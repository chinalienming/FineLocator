import json
import common


# dictionary 'id_methods_dic' and 'vec_dic':
#      id_methods_dic = {id : method}
#             vec_dic = {id : vec}
# reduce the cost of disk storage and memory use.
def update_methods_dic(method, value, id_method_dic, id_value_dic):
    if method in id_method_dic.values():
        print(method, 'already in id_method_dic.')
    else:
        new_id = len(id_method_dic) + 1
        id_method_dic[new_id] = method
        id_value_dic[new_id] = value


def update_id_method_dic(id_method_dic, method_id_dic, method):
    if method in method_id_dic:
        return method_id_dic[method]
    else:
        new_id = len(id_method_dic) + 1
        id_method_dic[new_id] = method
        method_id_dic[method] = new_id
        return new_id


def load_dic(path):
    with open(path, 'r') as f:
        dic = json.loads(f.read())
    return dic


def sstp_iterator(path):
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            sstp_id, value_str = line.split(common.sstp_external_splitor)
            ss, tp = value_str.split(common.sstp_internal_splitor)
            yield sstp_id, float(ss), float(tp)


def write_dic(path, dic):
    with open(path, 'w') as f:
        f.write(json.dumps(dic))
    return


def find_k_by_v(dic, value):
    k_list = [k for k, v in dic.items() if v == value]
    if len(k_list) > 0:
        return k_list[0]
    else:
        return None


def compare_dic(dic1, dic2):
    len1 = len(dic1)
    len2 = len(dic2)
    if len1 != len2:
        print('length:', len1, len2)
        return False
    else:
        for key in dic1:
            if key not in dic2:
                print('key:', key, 'not exists')
                return False
            else:
                v1 = dic1[key]
                v2 = dic2[key]
                if v1 != v2:
                    print('key =', key, 'v1 =', v1, 'v2 =', v2)
                    return False
                continue
        return True

# dic1 = {1:'aaa', 2:'bbb', 3:'ccc'}
# dic2 = {1:'aaa', 2:'bbb', 3:'ccc'}
# dic3 = {1:'aaa', 2:'bb', 3:'ccc'}
# print(compare_dic(dic1, dic3))

# dic = {1:0.1, 2:0.2}
# import json
# with open('test.dic', 'w') as f:
#     f.write(json.dumps(dic))
#
# with open('test.dic', 'r') as ff :
#     ss_dic = json.loads(ff.read())
#
# print(ss_dic["1"])




