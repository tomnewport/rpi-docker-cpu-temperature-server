from time import sleep
import subprocess
import re
import redis
import logging

logging.basicConfig(level=logging.DEBUG)


def check_cpu_temperature():
    raw_output = subprocess.check_output(
        ["/opt/vc/bin/vcgencmd", "measure_temp"]
    ).decode()
    output_matching = re.search("temp=([\d\.]+)'C", raw_output)
    return float(output_matching.group(1))

def update_temperature(redis_connection):
    current_temperature = check_cpu_temperature()
    redis_connection.set("currentCPUTemperature", current_temperature)

if __name__ == "__main__":
    logging.info("Checking Temperature")
    logging.info(check_cpu_temperature())
    redis_connection = redis.StrictRedis(host='redis', port=6379, db=0)
    logging.info("Starting loop")
    while True:
        update_temperature(redis_connection)
        logging.info(redis_connection.get("currentCPUTemperature"))
        sleep(5)


