#!/usr/bin/env python
# -*- coding: utf-8 -*-

import builtins
import collections
import sys
import traceback

"""
Programming
Final assignment 3: Bagagekluizen
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
Lever je werk in op Canvas als alle tests slagen.
"""

# Some configuration stuff
inputFile = "fa_testkluizen.txt"
lockerMax = 14
debug = True
testing = True

# FileNotFoundError prevention
try:  # Try opening the file
    open(inputFile, 'r').close()
except FileNotFoundError:  # If there's no file, create it
    print(f"\n\033[91m\033[1m  W A R N I N G   \033[0m {inputFile} was not found! New file of same name created...\n")
    open(inputFile, 'w').close()


def aantal_kluizen_vrij():
    with open(inputFile, "r") as lockerFile:
        lockersInUse = lockerFile.readlines()
    return lockerMax-len(lockersInUse)  # Return unused locker amount


"""    
    # Alternative code:
    return 12-len(open(inputFile, "r").readlines()))
    # Old code:
    kluisjesInGebruik = kluisjesInGebruik.read().strip('').split('\n') # Open, read file, strip trailing whitespaces, split line ends
    print(kluisjesInGebruik) # debug code
    return 12 - len(kluisjesInGebruik)
    # Must use open and close according to the 
"""


def nieuwe_kluis():
    lockerFile = open(inputFile)
    lockers = []
    for lines in lockerFile:
        if ";" in lines:
            lockerNumberEnd = lines.find(';')
            lockers.append(lines[:lockerNumberEnd])
            # kluisjes.sort()  # Might be fun to do when I've got some time left.
    lockerFile.close()
    i = 1  # Counting Integer
    while i <= lockerMax:
        if str(i) not in lockers:
            # print(i) # debug
            print(f"Kluisje {i} is beschikbaar. ")
            code = input("Stel kluiscode in... (Minimaal 4 tekens en geen ; ) ")
            if ';' in code or len(code) < 4:
                print("ERROR  Code was te kort of bevat ; ")
                return -1
            with open(inputFile, 'a') as lockerFile:
                lockerFile.write(f"{i};{code}\n")
            return i
        else:
            i += 1
    print("ERROR  Alle kluisjes zijn bezet!")
    return -2


def kluis_openen():
    lockerNumber = input("Wat is uw kluisnummer? ")
    lockerCode = input("Wat is uw kluiscode?" )
    lockerFormated = f"{lockerNumber};{lockerCode}"
    lockerFile = open(inputFile)
    lockerText = lockerFile.read()
    if lockerFormated in lockerText:
        print(f"Kluis {lockerNumber} is nu open.")
        return True
    else:
        print("Nummer of code is fout.")
        return False


def kluis_teruggeven():
    """
    Laat de gebruiker een kluisnummer invoeren, en direct daarna de bijbehorende
    kluiscode. Indien deze combinatie voorkomt in het tekstbestand met de kluizen
    die in gebruik zijn, moet deze combinatie/regel uit het tekstbestand verwijderd
    worden.

    Als het lukt om de combinatie te vinden en te verwijderen, is het resultaat
    van de functie True, anders False.

    Returns:
        bool: True als er een kluiscombinatie verwijderd werd, anders False
    """
    lockerNumber = input("Wat is uw kluisnummer? ")
    lockerCode = input("Wat is uw kluiscode?" )
    lockerFormated = f"{lockerNumber};{lockerCode}"
    print(lockerFormated)
    lockerFile = open(inputFile)
    lockerText = lockerFile.readlines()
    if lockerFormated in lockerText:
        print(f"Kluis {lockerNumber} is nu open.")
        lockerFile.close()
        lockerFile = open(inputFile, 'w')
        for line in lockerText.split('\n'):
            if line != lockerFormated:
                lockerFile.write(f"{line}\n")
        lockerFile.close()
        return True
    else:
        print("Nummer of code is fout.")
        return False
    # Optional, I'll do when I have the time and energy.
    """input("\n\n\n   It said it's not implemented, go back!\n"
          "   Press ENTER to continue...\n\n\n")"""
    return


def development_code():
    print(f"\033[94m=== Debug value's ===\n"
          f"InputFile = {inputFile} , LockerMax = {lockerMax}\n"
          f"Debug = {debug} , Testing = {testing}\033[0m")
    while True:
        print("\n"
              "1: Ik wil weten hoeveel kluizen nog vrij zijn\n"
              "2: Ik wil een nieuwe kluis\n"
              "3: Ik wil even iets uit mijn kluis halen\n"
              "# 4: Ik geef mijn kluis terug\n"
              "5: Ik wil stoppen")
        try:
            keuze = int(input())
            if keuze == 1:
                aantal_kluizen_beschikbaar = aantal_kluizen_vrij()
                print(f"Er zijn {aantal_kluizen_beschikbaar} kluizen beschikbaar.")
            elif keuze == 2:
                nieuwe_kluis()
            elif keuze == 3:
                kluis_openen()
            elif keuze == 4:
                kluis_teruggeven()
            elif keuze == 5:
                print("Exiting debug menu...")
                break
        except ValueError:
            print("!!! ERROR !!!  Input was geen Integer")


def module_runner():
    if debug:
        development_code()  # Comment deze regel om je 'development_code' uit te schakelen
    if testing:
        __run_tests()       # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __my_assert_args(function, args, expected_output, check_type=False):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output).__name__} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    if str(expected_output) == str(output):
        msg = f"Fout: {function.__name__}{argstr} geeft {output} ({type(output).__name__}) " \
              f"in plaats van {expected_output} (type {type(expected_output).__name__})"
    else:
        msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"

    if type(expected_output) is float and isinstance(output, (int, float, complex)):
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def __my_test_file():
    return "fa_testkluizen.txt"


def __create_test_file(safes, testfile=__my_test_file()):
    kluis_mv_ev = 'kluis' if len(safes) == 1 else 'kluizen'
    print(f"Voor testdoeleinden wordt bestand {testfile} aangemaakt met {len(safes)} {kluis_mv_ev}... ", end="")

    try:
        with open(testfile, 'w') as dummy_file:
            for number, code in safes:
                dummy_file.write(f"{number};{code}\n")
    except:
        print(f"\nFout: bestand {testfile} kon niet worden aangemaakt. Python-error:")
        print(traceback.format_exc())
        sys.exit()

    print("Klaar.")


def test_aantal_kluizen_vrij():
    function = aantal_kluizen_vrij

    case = collections.namedtuple('case', 'safes')
    testcases = [case(((11, "6754"),)),
                 case(((11, "6754"), (1, "geheim"), (12, "z@terd@g"))),
                 case(((1, "0000"), (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000"),
                       (2, "0000"), (4, "0000"), (6, "0000"), (8, "0000"), (10, "0000"), (12, "0000")))]

    for test in testcases:
        __create_test_file(test.safes)

        original_open = builtins.open
        builtins.open = lambda file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None: \
            original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline, closefd=closefd, opener=opener)

        try:
            expected_output = 12 - len(test.safes)
            __my_assert_args(function, (), expected_output, check_type=True)
        finally:
            builtins.open = original_open


def test_nieuwe_kluis():
    function = nieuwe_kluis

    case = collections.namedtuple('case', 'safes simulated_input possible_outputs')
    testcases = [case(((11, "6754"), (12, "z@terd@g")), ["geheim"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                 case(((1, "0000"), (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000"),
                       (2, "0000"), (4, "0000"), (6, "0000"), (8, "0000"), (10, "0000"), (12, "0000")), ["geheim"], [-2]),
                 case(((1, "0000"), (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000"),
                       (2, "0000"), (4, "0000"), (6, "0000"), (8, "0000"), (12, "0000")), ["geheim"], [10]),
                 case(((1, "0000"), (3, "0000")), ["abc"], [-1])]

    for test in testcases:
        __create_test_file(test.safes)

        original_open = builtins.open
        builtins.open = lambda file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None: \
            original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline, closefd=closefd, opener=opener)

        original_input = builtins.input
        simulated_input = test.simulated_input.copy()
        simulated_input.reverse()
        builtins.input = lambda prompt="": simulated_input.pop()

        try:
            output = function()

            assert isinstance(output, int), f"Fout: {function.__name__}() geeft {type(output).__name__} in plaats van int"
            assert output in test.possible_outputs, f"Fout: {function.__name__}() geeft {output}, maar mogelijke outputs zijn alleen: {test.possible_outputs}"

            # if all possible safenumbers are positive, a new safenumber should be registered by now
            if all(possible_safe_number > 0 for possible_safe_number in test.possible_outputs):
                free_safes = aantal_kluizen_vrij()
                expected_free_safes = 12 - (len(test.safes) + 1)

                msg = f"Fout: {function.__name__}() geeft aan dat een nieuwe kluis (nummer {output}) gereserveerd is, maar " \
                      f"daarna geeft aantal_kluizen_vrij() {free_safes} ipv {expected_free_safes}. Check evt. {__my_test_file()}"

                assert free_safes == expected_free_safes, msg

        except AssertionError as ae:
            raise AssertionError(f"{ae.args[0]}\n -> Info: gesimuleerde input voor deze test: {test.simulated_input}.") from ae
        except IndexError:
            raise AssertionError(f"Fout: er werd in de functie vaker om input gevraagd dan verwacht. Gesimuleerde input: {test.simulated_input}")
        finally:
            builtins.input = original_input
            builtins.open = original_open


def test_kluis_openen():
    function = kluis_openen

    case = collections.namedtuple('case', 'safes simulated_input expected_output')
    testcases = [case(((11, "6754"), (12, "z@terd@g")), ["11", "6754"], True),
                 case(((11, "6754"), (12, "z@terd@g")), ["10", "6754"], False)]

    for test in testcases:
        __create_test_file(test.safes)

        original_open = builtins.open
        builtins.open = lambda file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None: \
            original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline, closefd=closefd, opener=opener)

        original_input = builtins.input
        simulated_input = test.simulated_input.copy()
        simulated_input.reverse()
        builtins.input = lambda prompt="": simulated_input.pop()

        try:
            __my_assert_args(function, (), test.expected_output, check_type=True)
        except AssertionError as ae:
            raise AssertionError(f"{ae.args[0]}\n -> Info: gesimuleerde input voor deze test: {test.simulated_input}.") from ae
        except IndexError:
            raise AssertionError(f"Fout: er werd in de functie vaker om input gevraagd dan verwacht. Gesimuleerde input: {test.simulated_input}")
        finally:
            builtins.input = original_input
            builtins.open = original_open


def test_kluis_teruggeven():
    function = kluis_teruggeven

    case = collections.namedtuple('case', 'safes simulated_input expected_output')
    testcases = [case((), ["1", "geheim"], False),
                 case(((11, "6754"), (12, "z@terd@g")), ["12", "z@terd@g"], True),
                 case(((11, "6754"), (12, "z@terd@g")), ["11", "6754"], True),
                 case(((11, "6754"),), ["11", "6754"], True)]

    for test in testcases:
        __create_test_file(test.safes)

        original_open = builtins.open
        builtins.open = lambda file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None: \
            original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline, closefd=closefd, opener=opener)

        original_input = builtins.input
        simulated_input = test.simulated_input.copy()
        simulated_input.reverse()
        builtins.input = lambda prompt="": simulated_input.pop()

        try:
            __my_assert_args(function, (), test.expected_output, check_type=True)

            if test.expected_output:  # safe should be available again
                free_safes = aantal_kluizen_vrij()
                expected_free_safes = 12 - (len(test.safes) - 1)

                msg = f"Fout: {function.__name__}() geeft aan dat kluis (nummer {test.simulated_input[0]}) vrijgegeven is, maar " \
                      f"daarna geeft aantal_kluizen_vrij() {free_safes} ipv {expected_free_safes}."

                assert free_safes == expected_free_safes, msg

        except AssertionError as ae:
            raise AssertionError(f"{ae.args[0]}\n -> Info: gesimuleerde input voor deze test: {test.simulated_input}.") from ae
        except IndexError:
            raise AssertionError(f"Fout: er werd in de functie vaker om input gevraagd dan verwacht. Gesimuleerde input: {test.simulated_input}")
        finally:
            builtins.input = original_input
            builtins.open = original_open


def __run_tests():
    """ Test alle functies. """
    test_functions = [test_aantal_kluizen_vrij,
                      test_nieuwe_kluis,
                      test_kluis_openen,
                      # Uncomment de regel hieronder om ook de optionele functie kluis_teruggeven te testen:
                      #test_kluis_teruggeven
                     ]

    try:
        for test_function in test_functions:
            func_name = test_function.__name__[5:]

            print(f"\n======= Test output '{test_function.__name__}()' =======")
            test_function()
            print(f"Je functie {func_name} werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()
