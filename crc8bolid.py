# Расчет контрольной суммы для ключа в виде 000000AAAAAA
import binascii
import crcmod.predefined

def crc(byte_str):
    # Устанавливаем тип кодировки. Для Болида это crc-8-maxim
    crc8 = crcmod.predefined.mkPredefinedCrcFun('crc-8-maxim')
    # Меняем порядок записи ключа. Реверсируем
    byte_str_reverse = byte_str
    for _ in range(int(len(byte_str) / 2) - 1):
        byte_str_reverse = byte_str_reverse[0:_ * 2] + byte_str_reverse[-2:] + byte_str_reverse[_ * 2:-2]
    # Добавляем служебный бит
    byte_str_reverse = b'01'+bytes(byte_str_reverse, 'ascii')
    # Высчитываем контрольную сумму
    a = hex(crc8(binascii.unhexlify(byte_str_reverse)))
    return bytes(a[2:].upper()+byte_str.upper()+'01','ascii')



if __name__ == '__main__':
    print(crc('00550073D712'))
    print(crc('00000018B613'))
    print(crc('000000A434CB'))