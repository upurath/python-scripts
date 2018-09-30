def remove_empty_values(the_list):
    """ remove keys without values from a list of dictionaries
        Changes the list passed as an argument!
    """
    for d in the_list:
        # force keys into a list to work on
        for key in list(d.keys()):
            # use truthyness to identify keys without value attached
            if not d[key]:
                del d[key]

def sort_list_of_dicts(the_list, the_key, reverse_bool=False):
    """ sort a list of dictionaries by the values attached to a given key """
    sorted_list = sorted(the_list, key=lambda k: k[the_key], reverse=reverse_bool)
    return sorted_list
