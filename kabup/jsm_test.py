import jsm


if __name__ == "__main__" :
    q = jsm.Finance()
    yahoo = q.get(4689).round_lot
    print(yahoo)
    
