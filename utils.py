from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_count_except(counter, exception):
    keys = []
    results = []
    for key in counter:
        if key == exception:
            continue
        keys.append(key)
        results.append(counter[key])
    return keys, results


def count_cols(series):
    counter = Counter()
    for item in series:
        counter.update(item.split(', '))
    return counter


def generate_hbar(x, y, xlabel, ylabel, title):
    plt.figure(figsize=(20,10))
    x_pos = [i for i, _ in enumerate(x)]
    plt.barh(x_pos, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.yticks(x_pos, x)
    plt.title(title)
    plt.show()

def generate_hbar_subplot(x, y, xlabel, ylabel, title, ax):
    x_pos = [i for i, _ in enumerate(x)]
    ax.barh(x_pos, y)
    ax.set(xlabel=xlabel)
    ax.set(ylabel=ylabel)
    ax.set_yticks(x_pos)
    ax.set_yticklabels(x)
    ax.set_title(title)


def get_nested_values(series):
    results = set()
    for item in series:
        results.update(item.split(', '))
    return list(results)


def filter_by_language(df, value):
    result = []
    for col in df['language_used']:
        if value in col.split(', '):
            result.append(True)
        else:
            result.append(False)
    return result


def filter_by_ide(df, value):
    result = []
    for col in df['ide_used']:
        if value in col.split(', '):
            result.append(True)
        else:
            result.append(False)
    return result


def filter_by_field(field, df, value):
    result = []
    for col in df[field]:
        if value in col.split(', '):
            result.append(True)
        else:
            result.append(False)
    return result



def load_data(file_name):
    df = pd.read_csv("devkami_survey.tsv",sep="\t")
    remap_columns = {
        'What language do you use': 'language_used',
        'What kind of application do you build?': 'application_built',
        'What OS you deployed to': 'os_deployed',
        'What OS you write your code on': 'os_coded',
        'What IDE do you use': 'ide_used',
        'What Version control do you use': 'vcs_used',
        'How do you test your application?': 'app_test',
        'Tell us more about your development setup. Tell us things like the plugin you use on your IDE, whether you use docker or kubernetes, do you code using remote development tools etc.': 'dev_setup',
        'Tell us about your computer. Tell us about the spec, which model etc': 'computer_model',
        'How do you deploy your application? Tell us whether you build an docker image or use a script etc.': 'deploy_method',
        'What issue tracker you use in your team?': 'tracker_used',
        'Do you do standup in your work place': 'standup',
        'Do your team do sprint planning': 'sprint_planning',
        'Tell us more about your development process. What else your team do other than standup and sprint planning': 'dev_process',
    }

    df.rename(columns=remap_columns, inplace=True)
    df.replace(np.nan,'n/a',inplace=True)

    return df

