import unittest


class Numero:
    DESCRIPCION_DE_ERROR_DE_DIVISION_POR_CERO = "No se puede dividir por 0"

    def is_zero(self):
        self.shouldBeImplementedBySubclass()

    def is_one(self):
        self.shouldBeImplementedBySubclass()

    def is_negative(self):
        self.shouldBeImplementedBySubclass()

    def __add__(self, adder):
        self.shouldBeImplementedBySubclass()

    def __mul__(self, multiplier):
        self.shouldBeImplementedBySubclass()

    def __truediv__(self, divisor):
        self.shouldBeImplementedBySubclass()

    def __sub__(self, subtrahend):
        self.shouldBeImplementedBySubclass()

    def negated(self):
        return self * Entero.with_value(-1)

    def floor_division(self, aDivisor):
        self.shouldBeImplementedBySubclass()

    def __str__(self):
        import io

        output = io.StringIO()
        self.print_on(output)
        return output.getvalue()

    def print_on(self, a_stream):
        self.shouldBeImplementedBySubclass()

    def shouldBeImplementedBySubclass(self):
        raise NotImplementedError("Should be implemented by the subclass")


class Entero(Numero):
    DESCRIPCION_DE_ERROR_DE_FIBONACCI_NEGATIVO = (
        " Fibonacci no está definido aquí para Enteros Negativos"
    )

    def __init__(self, value):
        self._value = value

    @classmethod
    def with_value(cls, value):
        number = cls(value)
        return number

    def value(self):
        return self._value

    def is_zero(self):
        return self._value == 0

    def is_one(self):
        return self._value == 1

    def is_negative(self):
        return self._value < 0

    def __eq__(self, anObject):
        if isinstance(anObject, self.__class__):
            return self._value == anObject._value
        else:
            return False

    def __add__(self, adder):
        return Entero.with_value(self._value + adder.value())

    def __mul__(self, multiplier):
        return Entero.with_value(self._value * multiplier.value())

    def __truediv__(self, divisor):
        return Fraccion.with_over(self, divisor)

    def __sub__(self, subtrahend):
        return Entero.with_value(self._value - subtrahend.value())

    def fibonacci(self):
        one = Entero.with_value(1)
        two = Entero.with_value(2)

        if self.is_negative():
            raise ValueError(self.DESCRIPCION_DE_ERROR_DE_FIBONACCI_NEGATIVO)

        if self.is_zero() or self.is_one():
            return one

        return (self - one).fibonacci() + (self - two).fibonacci()

    def floor_division(self, aDivisor):
        return Entero.with_value(self._value // aDivisor.value())

    def greatest_common_divisor(self, otroEntero):
        if otroEntero.is_zero():
            return self
        else:
            return otroEntero.greatest_common_divisor(self.remainder_with(otroEntero))

    def remainder_with(self, divisor):
        return Entero.with_value(self._value % divisor.value())

    def print_on(self, a_stream):
        a_stream.write(str(self._value))


class Fraccion(Numero):

    def __init__(self, numerator, denominator):
        # Estas precondiciones estan por si se comenten errores en la implementacion - Hernan
        if numerator.is_zero():
            raise ValueError("Una fraccion no puede ser cero")
        if denominator.is_one():
            raise ValueError(
                "Una fraccion no puede tener denominador 1 porque sino es un entero"
            )

        self._numerator = numerator
        self._denominator = denominator

    @classmethod
    def with_over(cls, dividend, divisor):
        if divisor.is_zero():
            raise ValueError(cls.DESCRIPCION_DE_ERROR_DE_DIVISION_POR_CERO)
        if dividend.is_zero():
            return Entero.with_value(dividend.value())
        if divisor.is_negative():
            return cls(dividend.negated(), divisor.negated())

        greatest_common_divisor = dividend.greatest_common_divisor(divisor)
        numerator = dividend.floor_division(greatest_common_divisor)
        denominator = divisor.floor_division(greatest_common_divisor)

        if denominator.is_one():
            return Entero.with_value(numerator.value())

        return cls(numerator, denominator)

    def numerator(self):
        return self._numerator

    def denominator(self):
        return self._denominator

    def is_zero(self):
        return False

    def is_one(self):
        return False

    def is_negative(self):
        return self._numerator < 0

    def __eq__(self, anObject):
        if isinstance(anObject, self.__class__):
            return (
                self._numerator * anObject.denominator()
                == self._denominator * anObject.numerator()
            )
        else:
            return False

    def __add__(self, adder):
        nuevodenominator = self._denominator * adder.denominator()
        primeradder = self._numerator * adder.denominator()
        segundoadder = self._denominator * adder.numerator()
        nuevonumerator = primeradder + segundoadder

        return nuevonumerator / nuevodenominator

    def __mul__(self, multiplier):
        return (self._numerator * multiplier.numerator()) / (
            self._denominator * multiplier.denominator()
        )

    def __truediv__(self, divisor):
        return (self._numerator * divisor.denominator()) / (
            self._denominator * divisor.numerator()
        )

    def __sub__(self, subtrahend):
        newNumerator = (self._numerator * subtrahend.denominator()) - (
            self._denominator * subtrahend.numerator()
        )
        newDenominator = self._denominator * subtrahend.denominator()

        return newNumerator / newDenominator

    def floor_division(self, aDivisor):
        raise ValueError("Tipo de numero no soportado")

    def print_on(self, a_stream):
        a_stream.write(str(self._numerator))
        a_stream.write("/")
        a_stream.write(str(self._denominator))


class NumeroTest(unittest.TestCase):

    def setUp(self):
        self.zero = Entero.with_value(0)
        self.one = Entero.with_value(1)
        self.two = Entero.with_value(2)
        self.three = Entero.with_value(3)
        self.four = Entero.with_value(4)
        self.five = Entero.with_value(5)
        self.six = Entero.with_value(6)
        self.twenty_five = Entero.with_value(25)
        self.one_fifth = self.one / self.five
        self.two_fifths = self.two / self.five
        self.three_fifths = self.three / self.five
        self.two_twenty_fifths = self.two / self.twenty_five
        self.one_half = self.one / self.two
        self.five_halves = self.five / self.two
        self.six_fifths = self.six / self.five
        self.four_halves = self.four / self.two
        self.two_quarters = self.two / self.four

        self.negative_one = Entero.with_value(-1)
        self.negative_two = Entero.with_value(-2)

    def test01_is_zero_returns_true_when_ask_to_zero(self):
        self.assertTrue(self.zero.is_zero())

    def test02_is_zero_returns_false_when_ask_to_others_but_zero(self):
        self.assertFalse(self.one.is_zero())

    def test03_is_one_returns_true_when_ask_to_one(self):
        self.assertTrue(self.one.is_one())

    def test_04_is_one_returns_false_when_ask_to_other_than_one(self):
        self.assertFalse(self.zero.is_one())

    def test05_entero_adds_with_entero_correctly(self):
        self.assertEqual(self.two, self.one + self.one)

    def test06_entero_multiply_with_entero_correctly(self):
        self.assertEqual(self.four, self.two * self.two)

    def test07_entero_divides_entero_correctly(self):
        self.assertEqual(self.one, self.two / self.two)

    def test08_fraccion_adds_with_fraccion_correctly(self):
        # La suma de fracciones es:
        # a/b + c/d = (a.d + c.b) / (b.d)
        # SI ESTAN PENSANDO EN LA REDUCCION DE FRACCIONES NO SE PREOCUPEN!
        # NO SE ESTA TESTEANDO ESE CASO
        seven_tenths = Entero.with_value(7) / Entero.with_value(10)
        self.assertEqual(seven_tenths, self.one_fifth + self.one_half)

    def test_09_fraccion_multiplies_with_fraccion_correctly(self):
        # La multiplicacion de fracciones es:
        # (a/b) * (c/d) = (a.c) / (b.d)
        self.assertEqual(self.two_twenty_fifths, self.one_fifth * (self.two_fifths))

    def test10_fraccion_divides_fraccion_correctly(self):
        self.assertEqual(self.five_halves, self.one_half / self.one_fifth)

    def test11_entero_adds_fraccion_correctly(self):
        self.assertEqual(self.six / self.five, self.one + self.one_fifth)

    def test12_fraccion_adds_entero_correctly(self):
        self.assertEqual(self.six / self.five, self.one_fifth + self.one)

    def test13_entero_multiplies_fraccion_correctly(self):
        self.assertEqual(self.two_fifths, self.two * self.one_fifth)

    def test14_fraccion_multiplies_entero_correctly(self):
        self.assertEqual(self.two_fifths, self.one_fifth * self.two)

    def test15_entero_divides_fraccion_correctly(self):
        self.assertEqual(self.five_halves, self.one / self.two_fifths)

    def test16_fraccion_divides_entero_correctly(self):
        self.assertEqual(self.two_twenty_fifths, self.two_fifths / self.five)

    def test17_a_fraccion_can_be_equal_to_an_entero(self):
        self.assertEqual(self.two, self.four / self.two)

    def test18_aparent_fracciones_are_equal(self):
        self.assertEqual(self.one_half, self.two / self.four)

    def test19_adding_fracciones_can_return_an_entero(self):
        self.assertEqual(self.one, self.one_half + self.one_half)

    def test20_multiplying_fracciones_can_return_an_entero(self):
        self.assertEqual(self.one, (self.two / self.five) * (self.five / self.two))

    def test21_dividing_fracciones_can_return_an_entero(self):
        self.assertEqual(self.one, self.one_half / self.one_half)

    def test22_dividing_enteros_can_return_a_fraccion(self):
        self.assertEqual(self.one_half, self.two / self.four)

    def test23_can_not_divide_entero_by_zero(self):
        with self.assertRaises(Exception) as context:
            self.one / self.zero
        self.assertTrue(
            Numero.DESCRIPCION_DE_ERROR_DE_DIVISION_POR_CERO in str(context.exception)
        )

    def test24_can_not_divide_fraccion_by_zero(self):
        with self.assertRaises(Exception) as context:
            self.one_half / self.zero
        self.assertTrue(
            Numero.DESCRIPCION_DE_ERROR_DE_DIVISION_POR_CERO in str(context.exception)
        )

    def test25_a_fraccion_can_not_be_zero(self):
        self.assertFalse(self.one_half.is_zero())

    def test26_a_fraccion_can_not_be_one(self):
        self.assertFalse(self.one_half.is_one())

    def test27_entero_substracts_entero_correctly(self):
        self.assertEqual(self.two, self.three - self.one)

    def test28_fraccion_substracts_fraccion_correctly(self):
        self.assertEqual(self.one_fifth, self.two_fifths - self.one_fifth)

    def test29_entero_substracts_fraccion_correctly(self):
        self.assertEqual(self.one_half, self.one - self.one_half)

    def test30_fraccion_substracts_entero_correctly(self):
        six_fifths = self.six / self.five
        self.assertEqual(self.one_fifth, six_fifths - self.one)

    def test31_substracting_fracciones_can_return_an_entero(self):
        three_halves = self.three / self.two
        self.assertEqual(self.one, three_halves - self.one_half)

    def test32_substracting_same_enteros_returns_zero(self):
        self.assertEqual(self.zero, self.one - self.one)

    def test33_substracting_same_fracciones_returns_zero(self):
        self.assertEqual(self.zero, self.one_half - self.one_half)

    def test34_substracting_a_higher_value_to_a_number_returns_a_negative_number(self):
        negative_three_halves = Entero.with_value(-3) / self.two
        self.assertEqual(negative_three_halves, self.one - self.five_halves)

    def test35_fibonacci_zero_is_one(self):
        self.assertEqual(self.one, self.zero.fibonacci())

    def test36_fibonacci_one_is_one(self):
        self.assertEqual(self.one, self.one.fibonacci())

    def test37_fibonacci_entero_returns_adding_previous_two_fibonacci_enteros(self):
        self.assertEqual(self.five, self.four.fibonacci())
        self.assertEqual(self.three, self.three.fibonacci())
        self.assertEqual(
            self.five.fibonacci(), self.four.fibonacci() + self.three.fibonacci()
        )

    def test38_fibonacci_not_defined_for_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            negative_one = Entero.with_value(-1)
            negative_one.fibonacci()
        self.assertTrue(
            Entero.DESCRIPCION_DE_ERROR_DE_FIBONACCI_NEGATIVO in str(context.exception)
        )

    def test39_negation_of_entero_is_correct(self):
        self.assertEqual(self.negative_two, self.two.negated())

    def test40_negation_of_fraccion_is_correct(self):
        self.assertEqual((self.negative_one / self.two), self.one_half.negated())

    def test41_sign_is_correctly_assigned_to_fraction_with_two_negatives(self):
        self.assertEqual(self.one_half, (self.negative_one / self.negative_two))

    def test42_sign_is_correctly_assigned_to_fraction_with_negative_divisor(self):
        self.assertEqual(self.one_half.negated(), (self.one / self.negative_two))


if __name__ == "__main__":
    unittest.main()
