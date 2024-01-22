def conversion(blocks):
    for block in blocks:
        code = block_data[block["block_id"]]["code"]
        total_code = code.format(block["values"])
        print(total_code)


blocks = [{
        "block_type":"print",
        "block_id":"1",
        "values":"hello world"
    }
]
block_data = {
    "1":{
        "name":"print",
        "type":"block",
        "code":"print({})",
        "num_values":1
    }
}
conversion(blocks)