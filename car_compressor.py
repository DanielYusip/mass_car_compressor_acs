import json
import os
import py7zr
import logging
from datetime import datetime
from multiprocessing import Pool
from functools import partial

def get_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

def log_setup(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def zip_up_car(car_name, car_info, src_dir, out_dir, compression_lvl=None):
    car_folder = os.path.join(src_dir, car_name)
    
    if os.path.exists(car_folder):
        version = car_info.get('version', 'NoVer')
        archive_name = f"{car_name}_{version}.7z"
        archive_path = os.path.join(out_dir, archive_name)
        
        if os.path.exists(archive_path):
            logging.info(f"Skip {car_name}, done.")
            return

        try:
            if compression_lvl is not None:
                filters = [{'id': py7zr.FILTER_LZMA2, 'preset': compression_lvl}]
            else:
                filters = None  # Defaults filter, didn't test how they affect

            with py7zr.SevenZipFile(archive_path, 'w', filters=filters) as archive:
                archive.writeall(car_folder, car_name)
            logging.info(f"{car_name} zipped. Check your folder")
        except Exception as e:
            logging.error(f"{car_name} failed: {str(e)}")
    else:
        logging.warning(f"Warning, {car_name} folder MIA.")

def zip_all_cars(config):
    os.makedirs(config['out_dir'], exist_ok=True)

    try:
        with open(config['json_path'], 'r') as file:
            content = json.load(file)
    except FileNotFoundError:
        logging.error(f"No file: {config['json_path']}")
        return
    except json.JSONDecodeError:
        logging.error(f"Bad JSON: {config['json_path']}")
        return

    cars = content.get('cars', {})

    if not cars:
        logging.warning("No cars.")
        return

    zip_func = partial(zip_up_car, 
                       src_dir=config['src_dir'], 
                       out_dir=config['out_dir'],
                       compression_lvl=config.get('compression_lvl'))

    with Pool(processes=config['num_procs']) as pool:
        pool.starmap(zip_func, cars.items())

    logging.info("Finished. You can close this window now")

if __name__ == "__main__":
    config = get_config()
    log_setup(config['log_file'])

    start_time = datetime.now()
    logging.info(f"Start: {start_time}")
    
    zip_all_cars(config)