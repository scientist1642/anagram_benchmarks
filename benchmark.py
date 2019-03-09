import subprocess
import os
import json
import csv
import time
import sys
import statistics

RUN_COUNT = 30


def benchmark(sol_data, drop_cache):
    rpname = sol_data['repo']
    bench = {'lang': sol_data['lang']}

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
        bench['run_times'].append(int(float(time_micr)))

        if (drop_cache):
            time.sleep(2)
        time.sleep(1)

    return bench


def drop_cache():
    print('Clearing caches...')
    subprocess.check_output(
        ['sudo', 'sh', '-c',  'echo 3 > /proc/sys/vm/drop_caches'])
    time.sleep(3) #give some time to system


def benchmark_all(repo_name):
    if repo_name == 'all':
        benchmark_results = {}
    else:
        with open("benchmark_results.json", "r") as f:
            benchmark_results = json.load(f)

    with open("repos.txt") as f:
        csv_reader = csv.DictReader(f, delimiter='|', skipinitialspace=True)
        found = False
        for sol_data in csv_reader:
            if (repo_name == 'all' or repo_name == sol_data['repo']):
                drop_cache()
                benchmark_results[sol_data['repo']
                                  ] = benchmark(sol_data, False)
                found = True
        if not found:
            print('Repo name not found')

    with open("benchmark_results.json", "w") as f:
        json.dump(benchmark_results, f)


def generate_csv():
    with open("benchmark_results.json", "r") as f:
        result = json.load(f)
    with open("benchmark_results.csv", "w", newline='') as f:
        writer = csv.DictWriter(
            f, fieldnames=['repo', 'lang', 'mean', 'stdev'])
        writer.writeheader()
        row = {}
        for repo_name, data in result.items():
            row['repo'] = repo_name
            row['lang'] = data['lang']
            row['mean'] = int(statistics.mean(data['run_times']))
            row['stdev'] = int(statistics.stdev(data['run_times']))
            writer.writerow(row)


if __name__ == '__main__':
    benchmark_all(sys.argv[1])
    generate_csv()
