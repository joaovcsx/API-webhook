#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from base_handler import BaseHandler

class ContactModule(BaseHandler):

    def get(self, person_id=None):
        """Show person"""
        try:
            if person_id and int(person_id) == 1:
                self.response_send(self.get_contact(), 204)
            else:
                self.response_error(Exception('Bad Request', 400))
        except Exception as error:
            self.response_error(error)

    def post(self):
        print('caiuu')
        request_dict = self.request.POST
        print(request_dict)
        self.response_send(204)


    @staticmethod
    def get_contact():
        # headers = {
        #     'Accept': 'application/json',
        #     'Content-type':'application/json',
        #     'X-Imobzi-Secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aGlyZF9wYXJ0eV9hcHBfaWQiOjU4NTk0MDMyMSwiY3JlYXRlZF9hdCI6IjIwMjAtMDctMjhUMTc6NDk6NDQuOTUzMjcyWiIsImlzX3RoaXJkX3BhcnR5X2FjY2VzcyI6dHJ1ZX0.BBW19UzLkNVYqDsm4-divx6o6A2aV4m4DQiiRIKE-8w'}
        # contact = requests.get('https://api.imobzi.app/v1/person/6722714794459136', headers=headers)
        # print(contact)
        # return contact.content
        return {
            "code": "15",
            "landlord_account_id": "eb88da87e60611e9b3e773c4999d1a74",
            "review_pending": False,
            "media_source": "",
            "private": True,
            "manager": {"db_id": 6056164492050432,
            "type": "owner",
            "id": "yLSW3R739VbSDkcslx0Cha8Z5FR2",
            "user": {"fullname": "Jo\u00e3o Vitor",
            "db_id": "yLSW3R739VbSDkcslx0Cha8Z5FR2",
            "email": "joaovitor@quickfast.com",
            "profile_image_url": "https://firebasestorage.googleapis.com/v0/b/imobzi-app-production.appspot.com/o/users%2FyLSW3R739VbSDkcslx0Cha8Z5FR2%2Fprofile-photo?alt=media&token=9a35826b-106c-4393-971c-caa7811c48e3"}},
            "managers_shared": [],
            "bank_data": [{"bank_name": "Advanced Corretora de C\u00e2mbio Ltda",
            "account": "00000",
            "account_type": "checking_account",
            "bank_code": "117",
            "notes": "",
            "agency": "00000",
            "bank_id": 5922617898827776,
            "linked_to_lease": True,
            "id": 5741568698875904}, {"bank_name": "Advanced Corretora de C\u00e2mbio Ltda",
            "account": "111111",
            "account_type": "checking_account",
            "bank_code": "117",
            "notes": "",
            "agency": "1111",
            "bank_id": 5922617898827776,
            "linked_to_lease": False,
            "id": 6368497330290688}],
            "network_group_member_shared": False,
            "properties": [{"status": "available",
            "code": "5064",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/k980htsVuKVsOWQiME1_cvorq_JEm9afj8WWkysb1QavYJC9zFhG8fPL6Ihisd3z48hId7ZfJWCQwwt0u7bd96kF7vx3YHJJp5qrmmYwbQ=s0",
            "db_id": 537210431},
            "db_id": 4566704057221120,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa 7",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2000.0}, {"status": "rented",
            "code": "70",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/8BetvhyP-pKGbsvYYB3i9pSkdCbHBVxNmXTJ8nGSXy_taqzDP8uvnhaj1bfsxKzEKxd-BHyPFhwac5hQH4idVM_GrOnLm8UBWa7S3i_e=s0",
            "db_id": 528270714},
            "db_id": 4619992213487616,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 10000.0}, {"status": "rented",
            "code": "16",
            "neighborhood": "Fragoso",
            "cover_photo": {"url": "",
            "db_id": 0},
            "db_id": 4746985829564416,
            "address": "R. Angelim",
            "active": True,
            "city": "Olinda",
            "address_complement": "Apt 52",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 1800.0}, {"status": "rented",
            "code": "189",
            "neighborhood": "Parque Imperial",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/cX9ZXUns6lIlx0tU-Rprty_8kj0FPgvB8GytaizUCnrcPJePJqx4V2oiBxxmST6XlZp5b4Q-uOzd1-ecEeEbBXdAETPCMoz-dclC5PjAzg=s0",
            "db_id": 531580618},
            "db_id": 4785646273036288,
            "address": "S\u00e3o Roque, 45",
            "active": True,
            "city": "Barueri",
            "address_complement": "Casa 01",
            "database": "ac-uomw181122udzf",
            "sale_value": 100000.0,
            "rental_value": 1500.0}, {"status": "rented",
            "code": "160",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/NRzOeDswhvtHn_hVmo4NVrbZd1mJ8EkqG6u1Knpw7o0VuSOBqBmCSUzL9xO0GPj_r-LQc8wXINvd7WjSH212vBbj54NbvLPnfwKt-D61",
            "db_id": 496140124},
            "db_id": 4996094261985280,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa1",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2500.0}, {"status": "rented",
            "code": "146",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/48XNQO4p1I8X9VZ4Hn-W1Ip8f35fi-tRnGGBw6zUQ-WfU295lC7xliQn5zGIINtPyDYz9iBNX-nRO4KjIGoYthkSrvguGx2w-nxwgrpUYaM=s0",
            "db_id": 508380273},
            "db_id": 5188299557699584,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa1",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2500.0}, {"status": "rented",
            "code": "188",
            "neighborhood": "Jardim Maria Sampaio",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/Uz459wojhc7G6qXfiFv1yVkujfcP275lJvJQTNCfjM-_Yu7FgLHydM7FUmnN6lSEx1pm2PJzF0Agsmmtu-LCCW5DZCLE8IS1UlAIhGQ3HA=s0",
            "db_id": 517771283},
            "db_id": 5243702119235584,
            "address": "Rua Doutor Jorge Arida",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "",
            "database": "ac-uomw181122udzf",
            "sale_value": 500000.0,
            "rental_value": 1500.0}, {"status": "rented",
            "code": "203",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/GyxV54RUZ1zi7a_BGDNmbLL8QcNBD57FMlO57Ofl1UxB_CQTD_XJ3847FIlhY1QAMNPnRq2Z6881UPniLrl7ANT-keaL4nJIYj8JTeAgqg=s0",
            "db_id": 518921118},
            "db_id": 5358132899348480,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa1",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2500.0}, {"status": "available",
            "code": "206",
            "neighborhood": "Centro Hist\u00f3rico de S\u00e3o Paulo",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/G7kqVZ_xPzDK2CDBEHzLCWd4qdTsJqj-6m7IftrA02ZG1ztXjWgb-jWjCvTYcvy-bCgNu2u_CXxjHzEHCFiFa1hJk0I-fWl7UPjkdTjEdFs",
            "db_id": 528460049},
            "db_id": 5410130390679552,
            "address": "Rua 25 de Mar\u00e7o",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "",
            "database": "ac-uomw181122udzf",
            "sale_value": 420000.0,
            "rental_value": 3500.0}, {"status": "rented",
            "code": "200",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/yd1fXvlHkXDEQsY3gXNFRJ5tPSrrMtL3kFgCix3k_PWE6_IyenkYAM3kbRui0oCIhp7MXOz6GHzZikqlzgTqEJKzjsTdDPwS1Cpa2Bh7oFg",
            "db_id": 516983444},
            "db_id": 5530255720710144,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa1",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2500.0}, {"status": "rented",
            "code": "161",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/8J0fQCPRiD3EEHegzozqM8AhWqDjVF4MuFrsXHeaegA3rfzKoQ1EttwfPw-JOO0u_iDlTfgmXnRzSkmfeZN0Po23ibAUR0m-mCwv2g6-OA",
            "db_id": 486670002},
            "db_id": 5568121763004416,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa1",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2500.0}, {"status": "rented",
            "code": "191",
            "neighborhood": "Parque Imperial",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/YeXl_5jVX6q1qkWYHWIKvnLA7f5ihuhy1XXKtUVsHnJ-X4DSxm9yEKCvDJ2jpw9LQKoRHYhWqpFzB37nl_fI1bc2dqjq9obzIg79ettP=s0",
            "db_id": 525860087},
            "db_id": 5570142652071936,
            "address": "S\u00e3o Roque, 45",
            "active": True,
            "city": "Barueri",
            "address_complement": "Casa 02",
            "database": "ac-uomw181122udzf",
            "sale_value": 100000000.0,
            "rental_value": 1.0}, {"status": "rented",
            "code": "174",
            "neighborhood": "Vila da Paz",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/RDUT-Ec4AR_tALkMnDoH_lkA19L505Pdm9NL5msrlQwZG1tTOtPnPNybzm32ZDqaCTvcPudREQWr7_eEBANKiN2yAQkjLDk7zrvvXv5Mqg",
            "db_id": 496690070},
            "db_id": 5772754043273216,
            "address": "Av. Jo\u00e3o Paulo da Silva",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "61 bloco 1",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 3300.0}, {"status": "rented",
            "code": "202",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/VBOGwQVHLDXiQWPzT__M4j5uQrarpkK7op5UWtfegxWmrcT93wyey9L-n0wqZj8kt01M0lHmRqx6_ws9sKDoRlG78Krhc6fiN3UzaJ3IJ2Q",
            "db_id": 494340943},
            "db_id": 5787241202843648,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa1",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2500.0}, {"status": "rented",
            "code": "205",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/Phn9Os72Em2cuChb-htcSntBordZ5GYEStvdYKEIHze5n2CZwz0rjDkHIlMijONqpshStxSN_kQNZa_oSw9szmQ-TtzK2uffPwJwQOe7ig",
            "db_id": 500210065},
            "db_id": 5792689838620672,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa1",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2500.0}, {"status": "available",
            "code": "71",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "",
            "db_id": 0},
            "db_id": 5915779182624768,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2000.0}, {"status": "available",
            "code": "5072",
            "neighborhood": "Jardim Germ\u00e2nia",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/1KIWjw8YFnS4sy-wriD81Ulle6XU7gOWGmL3Q6Wk0XnVFhMqOXYllYRoXsLQU2_0YxlzCvIiiRoYobiGutwfuly109_SK3q9Tn8zdPO_",
            "db_id": 574871100},
            "db_id": 6015905211351040,
            "address": "R. \u00darsula de Camargo Barros",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa 05",
            "database": "ac-uomw181122udzf",
            "sale_value": 450000.0,
            "rental_value": 3500.0}, {"status": "rented",
            "code": "111",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/Zuemzs5H3karIOaGPsjeiS7UmiQeWb7NXcYJadcwf15_hJOxCcZLFzbNNJkYt7tsj9UV6Liuhn9Ghhfwz289SwEyZ-AIPj5X2-JKKgHPSHc=s0",
            "db_id": 373430094},
            "db_id": 6016873963454464,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa1",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2500.0}, {"status": "available",
            "code": "172",
            "neighborhood": "Jardim Germ\u00e2nia",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/1KIWjw8YFnS4sy-wriD81Ulle6XU7gOWGmL3Q6Wk0XnVFhMqOXYllYRoXsLQU2_0YxlzCvIiiRoYobiGutwfuly109_SK3q9Tn8zdPO_=s0",
            "db_id": 521400061},
            "db_id": 6341565251321856,
            "address": "R. \u00darsula de Camargo Barros",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa 05",
            "database": "ac-uomw181122udzf",
            "sale_value": 450000.0,
            "rental_value": 3500.0}, {"status": "rented",
            "code": "181",
            "neighborhood": "Jardim Germ\u00e2nia",
            "cover_photo": {"url": "",
            "db_id": 0},
            "db_id": 6370745494011904,
            "address": "R. \u00darsula de Camargo Barros",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa 05",
            "database": "ac-uomw181122udzf",
            "sale_value": 450000.0,
            "rental_value": 3500.0}, {"status": "rented",
            "code": "5055",
            "neighborhood": "Port\u00e3o",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/0rx90SpuH40mOSLroMXf75Psm2TiqWBR2I1XeG_xAH08kjbw6yzE0uaXdxysR2fmX9SUpBlhMuQRKCsB8c7TnGeXbTTogfFSA1xRzRhtkek=s0",
            "db_id": 543750215},
            "db_id": 6504301981597696,
            "address": "Rua Jo\u00e3o Bettega",
            "active": True,
            "city": "Curitiba",
            "address_complement": "ABCR",
            "database": "ac-uomw181122udzf",
            "sale_value": 1500000.0,
            "rental_value": 3500.0}, {"status": "rented",
            "code": "201",
            "neighborhood": "Jardim Iracema",
            "cover_photo": {"url": "https://lh3.googleusercontent.com/KOy2M_7ADUCcWQEiLlJBzeXGQMMoOepOqizzT5mzOjxIJcukydQ6z587iZ4q3Rs2tVE6PAaq9WkhO32Xofn02G0Scy_hZhBBZAkpcdNu",
            "db_id": 520890642},
            "db_id": 6561140890927104,
            "address": "Avenida Jacobus Baldi",
            "active": True,
            "city": "S\u00e3o Paulo",
            "address_complement": "casa1",
            "database": "ac-uomw181122udzf",
            "sale_value": 0.0,
            "rental_value": 2500.0}],
            "location": "-15.77972, -47.92972",
            "email": "joaovc.5814@gmail.com",
            "db_id": 6722714794459136,
            "firstname": "Joao",
            "tags": ["contact",
            "property-owner",
            "listing broker",
            "customer",
            "realtor",
            "renter"],
            "lastname": "Vitor",
            "organizations_associated": [],
            "profile_image_url": None,
            "social_network": [],
            "phone": {"type": "mobile",
            "number": "(11) 97965-5121",
            "country_code": "+55",
            "alpha2Code": "br"},
            "birthday": False,
            "db_key": "ahtwfmltb2J6aS1hcHAtcHJvZHVjdGlvbi1hcGlyEwsSBlBlcnNvbhiAgICa4Mj4CwyiARFhYy11b213MTgxMTIydWR6Zg",
            "persons_associated": [],
            "active": True,
            "emails": ["joaovc.5814@gmail.com",
            "joaovitor-15@live.com"],
            "cellphone": {"type": "mobile",
            "number": "(11) 97965-5121",
            "country_code": "+55",
            "alpha2Code": "br"},
            "fields": {"group_contact": [[{"name": "Comercial",
            "required": False,
            "field_id": "phone",
            "value": [{"type": "mobile",
            "number": "(11) 97965-5121",
            "country_code": "+55",
            "alpha2Code": "br"}],
            "position": "1",
            "configuration": {"typevalue": "json",
            "mask": "",
            "values": ["number",
            "type"],
            "showingroup": True,
            "validate": "",
            "type": "phone"}}], [{"name": "E-mail",
            "required": False,
            "field_id": "email",
            "value": ["joaovc.5814@gmail.com",
            "joaovitor-15@live.com"],
            "position": "2",
            "configuration": {"typevalue": "list",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+",
            "type": "email"}}], [{"name": "Site",
            "required": False,
            "field_id": "site",
            "value": None,
            "position": "3",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Site"}}]],
            "social_network": [[{"name": "social_network",
            "required": False,
            "field_id": "social_network",
            "value": [],
            "position": "4",
            "configuration": {"typevalue": "json",
            "mask": "",
            "values": [],
            "showingroup": True,
            "validate": "",
            "type": "social_network"}}]],
            "group_personal": [[{"name": "Nome Completo",
            "required": False,
            "field_id": "fullname",
            "value": "Joao Vitor",
            "position": "1",
            "configuration": {"typevalue": "fullname",
            "mask": "",
            "values": [""],
            "showingroup": False,
            "validate": "",
            "type": "Input"}}], [{"name": "CPF",
            "required": False,
            "field_id": "cpf",
            "value": "422.132.898-32",
            "position": "2",
            "configuration": {"typevalue": "cpf",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "\\d{3}\\.*\\d{3}\\.*\\d{3}-*\\d{2}",
            "type": "Cpf"}}], [{"name": "RG",
            "required": False,
            "field_id": "rg",
            "value": "50624855152",
            "position": "3.1",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Input"}}, {"name": "Data de emiss\u00e3o do RG",
            "required": False,
            "field_id": "rg_issue_date",
            "value": None,
            "position": "3.2",
            "configuration": {"typevalue": "",
            "mask": "dd/mm/yyyy",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Date"}}], [{"name": "Org\u00e3o emissor do RG",
            "required": False,
            "field_id": "rg_issue_organ",
            "value": None,
            "position": "4.1",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Input"}}, {"name": "Estado de emiss\u00e3o do RG",
            "required": False,
            "field_id": "rg_issue_state",
            "value": None,
            "position": "4.2",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Input"}}], [{"name": "Anivers\u00e1rio",
            "required": False,
            "field_id": "birthday",
            "value": "2020-05-06",
            "position": "5.1",
            "configuration": {"typevalue": "birthday",
            "mask": "dd/mm/yyyy",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Date"}}, {"name": "Estado Civil",
            "required": False,
            "field_id": "marital_status",
            "value": "Solteiro",
            "position": "5.2",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": ["Solteiro",
            "Casado",
            "Separado",
            "Divorciado",
            "Vi\u00favo",
            "Uni\u00e3o Est\u00e1vel"],
            "showingroup": True,
            "validate": "",
            "type": "marital_status"}}], [{"name": "Naturalidade",
            "required": False,
            "field_id": "place_of_birth",
            "value": "brasileiro",
            "position": "6.1",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Input"}}, {"name": "Nacionalidade",
            "required": False,
            "field_id": "nationality",
            "value": "Brasil",
            "position": "6.2",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Input"}}], [{"name": "Profiss\u00e3o",
            "required": False,
            "field_id": "profession",
            "value": None,
            "position": "7",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Input"}}], [{"name": "Sexo",
            "required": True,
            "field_id": "gender",
            "value": "Masculino",
            "position": "8",
            "configuration": {"typevalue": "gender",
            "mask": "",
            "values": ["Masculino",
            "Feminino"],
            "showingroup": False,
            "validate": "",
            "type": "Select"}}]],
            "group_address": [[{"name": "Endere\u00e7o",
            "required": False,
            "field_id": "address",
            "value": None,
            "position": "1",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Address"}}], [{"name": "Complemento",
            "required": False,
            "field_id": "address_complement",
            "value": None,
            "position": "2",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Input"}}], [{"name": "Bairro",
            "required": False,
            "field_id": "neighborhood",
            "value": None,
            "position": "3",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Neighborhood"}}], [{"name": "Cidade",
            "required": False,
            "field_id": "city",
            "value": None,
            "position": "4",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": ["S\u00e3o Paulo",
            "Belo Horizonte",
            "Florian\u00f3poles"],
            "showingroup": True,
            "validate": "",
            "type": "City"}}], [{"name": "state",
            "required": False,
            "field_id": "state",
            "value": None,
            "position": "5.1",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "State"}}, {"name": "CEP",
            "required": False,
            "field_id": "zipcode",
            "value": None,
            "position": "5.2",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "\\d{5}-*\\d{3}",
            "type": "CEP"}}], [{"name": "Pa\u00eds",
            "required": False,
            "field_id": "country",
            "value": None,
            "position": "6",
            "configuration": {"typevalue": "",
            "mask": "",
            "values": [""],
            "showingroup": True,
            "validate": "",
            "type": "Country"}}]]},
            "favorite": False,
            "associated_with": [],
            "fullname": "Joao Vitor"}