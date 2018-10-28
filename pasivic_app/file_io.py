import pandas


def get_file_extension(file):
    try:
        return str(file).rsplit(r'.')[1] 
    except IndexError:
        return None

def get_dataframe(file):
    extension = get_file_extension(file)
    return pandas.read_csv(file,sep=',',header=None) if extension=='csv' else pandas.read_excel(file,header=None)
        
