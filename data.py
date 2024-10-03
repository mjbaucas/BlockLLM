text_data_arr = [
    '''function Send{
        from: user_1,
        to: user_2,
        allow_transaction: true
    }
    ''',
    '''function Send{
        from: user_3,
        to: user_2,
        allow_transaction: true,
    }
    ''',
    '''function Send{
        from: user_3,
        to: user_1,
        allow_transaction: false
    }
    ''',    
    '''function Send{
        from: user_1,
        to: user_3,
        allow_transaction: true
    }
    ''',
    '''function Send{
        from: user_2,
        to: user_1,
        allow_transaction: true
    }
    ''',
    '''function Send{
        from: user_2,
        to: user_3,
        allow_transaction: false
    }
    ''',    
    '''function Send{
        from: user_4,
        to: user_2,
        allow_transaction: true
    }
    ''',
    '''function Send{
        from: user_4,
        to: user_3,
        allow_transaction: true
    }
    ''',
    '''function Send{
        from: user_4,
        to: user_1,
        allow_transaction: false
    }
    ''',
]
