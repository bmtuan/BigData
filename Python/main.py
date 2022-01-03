from hdfs import InsecureClient
from json import dump
from sodapy import Socrata
import argparse


parser = argparse.ArgumentParser(description='Arg for crawl')
parser.add_argument('--amount', help='amunt of samples')
parser.add_argument('--namenode', help='ip of namenode hdfs')
parser.add_argument('--path', help='path to save into hdfs')
args = parser.parse_args()

client = Socrata("data.iowa.gov", None)
print('crawling...')
results = client.get("cc6f-sgik", limit=args.amount)
client = InsecureClient(f'http://{args.namenode}:9870')

with client.write(f'{args.path}', encoding='utf-8') as writer:
    dump(results, writer)
print('done!!!!')
