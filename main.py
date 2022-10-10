import sys
from es import delete_log_later_days, get_log_later_days


if __name__ == '__main__':
    try:
        arg = sys.argv[3]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <url_domain> <index> <days>")
    print(arg[::-1])

    domain = sys.argv[1]
    indices = sys.argv[2]
    days = int(sys.argv[3])

    # count_data = -1
    # while count_data != 0:
    #     json_data = get_log_later_days(domain, indices, 6)
    #     data = json.loads(json_data)
    #     count_data = len(data['hits']['hits'])
    #     if count_data > 0:
    #         print('count data more than zero')

    #         for hit in data['hits']['hits']:
    #             # print(f'hit: {hit}')

    #             delete_data = delete_log_by_id(domain, indices, hit['_id'])
    #             print(f'delete: {delete_data}')
    #     else:
    #         print('no data to delete')

    delete_data = delete_log_later_days(domain, indices, days)
    print(f'delete: {delete_data}')

    get_data = get_log_later_days(domain, indices, days)
    print(f'data: {get_data}')

    print('complete')
