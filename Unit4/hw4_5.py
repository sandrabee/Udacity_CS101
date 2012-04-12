def split_string(source,splitlist):
    dest = source
    for delimiter in splitlist:
        dest = dest.replace(delimiter, ' ')
    return dest.split()

print split_string("_This__is___a____string_don't split me_____", "_")
