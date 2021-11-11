import json
import requests


class API:
    apikey = ""
    unique_trans = list()

    def __init__(self, key):
        self.apikey = key

    def do_request(self, url):
        r = requests.get(url=url)
        data = r.json()
        block = data['result']
        return block

    def write_to_file(self, json_obj, path):
        f = open(path, "a")
        f.write(json_obj)
        f.write('\n')
        f.close()

    def search_by_api(self, startpoint, endpoint):
        # add exception here
        if startpoint > endpoint:
            print("Error. Begin point must be less then end point")
        else:
            for i in range(startpoint, endpoint+1):

                tag = hex(i)
                url_to_get_block = f"https://api.velas.com/api?module=proxy&action=eth_getBlockByNumber&tag={tag}&boolean=true&apikey={self.apikey}"
                response_from_block = self.do_request(url_to_get_block)

                json_object = json.dumps(response_from_block, indent=4)
                file_path = "block.json"
                self.write_to_file(json_object, file_path)

                transactions_in_block = response_from_block['transactions']

                trans_hash = list()

                for i in range(len(transactions_in_block)):
                    trans_hash.append(transactions_in_block[i]['hash'])

                self.get_transactions(trans_hash)

    def get_transactions(self, trans_hash):
        tr_by_hash = list()

        for i in range(len(trans_hash)):
            tag_hash = trans_hash[i]

            url_get_trans_by_hash = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash={tag_hash}&apikey={self.apikey}"
            response_from_trans = self.do_request(url_get_trans_by_hash)

            tr_by_hash.append(response_from_trans)
            json_object1 = json.dumps(response_from_trans, indent=4)
            path_to_trans = "trans.json"
            self.write_to_file(json_object1, path_to_trans)

        list_from = list()
        for i in range(len(trans_hash)):
            list_from.append(tr_by_hash[i]['from'])

        split_list = self.split_str(list_from)
        unic_list = self.get_unique_transaction(split_list)
        #print(unic_list)
        for i in range(len(unic_list)):
            self.unique_trans.append(unic_list[i])

    def split_str(self, list_from):
        full_list = list()
        for i in range(len(list_from)):
            full_list.append(list_from[i].split(","))
        return full_list

    def get_unique_transaction(self, list_from):
        unique_numbers = list(self.get_unique_numbers((list_from)))
        return unique_numbers

    def get_unique_numbers(self, list):
        unique = []

        for number in list:
            if number in self.unique_trans:
                continue
            else:
                unique.append(number)
        return unique


api = API("YUXA3U56Y7EGFIBJVG8YJAU26FCFB9Y6Q6")
print("Hello! Please, enter range (in decimal number system)")
print("begin: ")
begin = int(input())
print("end: ")
end = int(input())
# api.search_by_api(68943, 68946)
api.search_by_api(begin, end)
if len(api.unique_trans)>0:
    print("Unique 'from': " + str(api.unique_trans))
    print("Count Of Unique: " + str(len(api.unique_trans)))
else:
    print("No transactions")
