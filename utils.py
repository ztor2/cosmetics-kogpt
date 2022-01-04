import json
import random


def textgen_option(temperature, avg_length):
    config = json.load(open('./model/config.json', 'r'))
    config['task_specific_params']['text-generation']['temperature'] = temperature
    config['task_specific_params']['text-generation']['max_length'] = \
        random.sample(range(avg_length - 20, avg_length + 21), 1)[0]
    json.dump(config, open('./model/config.json', 'w'))
    return print('temperature: {}, avg_length: {}'.format(temperature, avg_length))


def review_generate(keyword, generator, nums):
    if nums == 1:
        output = generator(keyword)[0]['generated_text']
    else:
        output = ''
        for i in range(nums):
            output += ('{}번째 리뷰:\n'.format(i + 1) + generator(keyword)[0]['generated_text'] + '\n\n')
    output = output.strip()
    return output
