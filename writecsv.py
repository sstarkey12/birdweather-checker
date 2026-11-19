import csv

def write_csv(file_path, data, append=True):
    """Write single row to csv file 

    Args:
        file_path (str): filename
        data (list): ['data1', 'datat2', 'data3']
        append (bool): True to append, False to overwrite
    """
    if append:
        open_mode = 'a'
    else:
        open_mode = 'w'
    with open(file_path, open_mode, newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
    csvfile.close()   
    

if __name__ == '__main__':
    pass