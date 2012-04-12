def new_procedure(htable, key, update):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key and update == None:
            return entry[1]
        elif entry[0] == key and update != None:
             entry[1] = update 
             return
    if update != None:
        bucket.append([key, update])
    return None

def hashtable_update(htable, key, value):
    new_procedure(htable, key, value)

def hashtable_lookup(htable, key):
    return new_procedure(htable, key, None)
