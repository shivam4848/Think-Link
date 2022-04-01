def get_paginated_list(results, url, limit, offset=0):
    offset = int(offset)
    limit = int(limit)
    count = len(results)
    if count < offset or limit < 0:
        return None
    obj = dict()
    obj['count'] = count
    offset_copy = max(1, offset - limit)
    limit_copy = offset
    obj['url'] = url + '?offset=%d&limit=%d' % (offset_copy, limit_copy)
    if offset + limit > count:
        obj['next'] = ''
    else:
        offset_copy = offset + limit
        obj['next'] = url + '?offset=%d&limit=%d' % (offset_copy, limit)
    obj['data'] = results[(offset):(offset + limit)]
    return obj
