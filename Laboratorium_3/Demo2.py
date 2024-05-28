import json
from numbers import Complex

def encode_complex(obj):
    if isinstance(obj, Complex):
        return {'__complex__': True, 'real': obj.real, 'imag': obj.imag}
    return obj

def decode_complex(obj):
    if '__complex__' in obj:
        return complex(obj['real'], obj['imag'])
    return obj


complex_number = 2 + 3j
encoded_complex = json.dumps(complex_number, default=encode_complex)

decoded_complex = json.loads(encoded_complex, object_hook=decode_complex)
print(decoded_complex)
