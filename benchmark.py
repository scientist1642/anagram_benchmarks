import subprocess
import os
import json
import csv
import time
import statistics

RUN_COUNT = 30


def benchmark(sol_data, drop_cache):
    rpname = sol_data['repo']
    bench = {'repo': rpname, 'lang': sol_data['lang']}

    bench['drop_cache'] = drop_cache
    bench['run_times'] = []

    for i in range(1, RUN_COUNT + 1):
        filepath = os.path.abspath('dictionaries/{}.txt'.format(i))
        command = 'cd {} && {} {} tere'.format('solutions/' + rpname,
                                               sol_data['exec'], filepath)

        # print(subprocess.check_output([command]))
        try:
            res = subprocess.check_output(
                ['bash', '-c', command]).decode('utf-8')
        except Exception as ex:
            print('error executing {}', rpname)
            print(ex)
            return {}

        time_micr = res.strip().split(',')[0]
        print('{} run #{} time {}'.format(rpname, i, time_micr))
        bench['run_times'].append(int(time_micr))

        if (drop_cache):
            time.sleep(2)
        time.sleep(1)

    return bench


def drop_cache():
    subprocess.check_output(
        ['sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"'])


def benchmark_all():
    benchmark_results = []
    with open("repos.txt") as f:
        csv_reader = csv.DictReader(f, delimiter='|', skipinitialspace=True)
        for sol_data in csv_reader:
            benchmark_results.append(benchmark(sol_data, False))

    with open("benchmark_results.json", "w") as f:
        json.dump(benchmark_results, f)


def generate_csv():
    with open("benchmark_results.json", "r") as f:
        results = json.load(f)
    with open("benchmark_results.csv", "w", newline='') as f:
        writer = csv.DictWriter(
            f, fieldnames=['repo', 'lang', 'mean', 'stdev'])
        writer.writeheader()
        row = {}
        for result in results:
            row['repo'] = result['repo']
            row['lang'] = result['lang']
            row['mean'] = int(statistics.mean(result['run_times']))
            row['stdev'] = int(statistics.stdev(result['run_times']))
            writer.writerow(row)


if __name__ == '__main__':
    benchmark_all()
    generate_csv()
