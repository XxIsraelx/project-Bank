import re
import sys


class Verificador:
    def __init__(self):
        pass

    def verificar(self, cpf: str) -> bool:
        """
        Verifica se um CPF é válido. 

        Parâmetros:
        cpf (str): CPF a ser verificado.

        Retorna:
        bool: True se o CPF for válido, False caso contrário.
        """
        # Limpa o CPF da entrada removendo caracteres não numéricos
        cpf_enviado_usuario = re.sub(r'[^0-9]', '', cpf)

        # Verifica se o CPF é uma sequência repetitiva (como "11111111111")
        if cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario):
            return False  # CPF é inválido se for uma sequência repetitiva

        # Verifica se o CPF possui exatamente 11 dígitos
        if len(cpf_enviado_usuario) != 11:
            return False  # CPF inválido se não tiver 11 dígitos

        # Calcula o primeiro dígito verificador
        nove_digitos = cpf_enviado_usuario[:9]
        resultado_digito_1 = sum(int(digito) * (10 - i) for i, digito in enumerate(nove_digitos))
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        # Calcula o segundo dígito verificador
        dez_digitos = nove_digitos + str(digito_1)
        resultado_digito_2 = sum(int(digito) * (11 - i) for i, digito in enumerate(dez_digitos))
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        # Gera o CPF completo com dígitos verificadores
        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

        # Compara o CPF gerado com o CPF enviado
        return cpf_enviado_usuario == cpf_gerado_pelo_calculo

Verificador().verificar('0246020407')
    