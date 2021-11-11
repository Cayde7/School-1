#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections, builtins


def inlezen_beginstation(stations):
    while True:
        beginstation = input("Beginstation: ")
        if beginstation in stations:  # als het station bestaat/in de lijst staat
            return beginstation
        else:
            print(beginstation + " is geen bestaand station.")


def inlezen_eindstation(stations, beginstation):
    while True:  # Infinite loop, break bij return of INTERRUPT SIGNAL (CTRL+C)
        eindstation = input("Eindstation: ")
        if eindstation in stations:  # als het station bestaat/in de lijst staat
            if stations.index(eindstation) > stations.index(beginstation):  # als het eindstation na het begin is
                return eindstation
            else:
                print(eindstation + " komt eerder dan het beginstation " + beginstation + "!")
        else:
            print(eindstation + " is geen bestaand eindstation.")


def omroepen_reis(stations, beginstation, eindstation):
    tussenstations= ""
    for x in stations:
        if stations.index(beginstation) < stations.index(x) < stations.index(eindstation):
            tussenstations += f"- {x}\n"
    return (f"Het beginstation {beginstation} is het {stations.index(beginstation)+1}e station in het traject.\n"
            f"{tussenstations}"
            f"Het eindstation {eindstation} is het {stations.index(eindstation)+1}e station in het traject.\n"
            f"De afstand bedraagt {stations.index(eindstation)-stations.index(beginstation)} station(s).\n"
            f"De prijs van het kaartje is {(stations.index(eindstation)-stations.index(beginstation))*5} euro.")
    # de \n voelt overbodig maar dat is het niet
    # deze opdracht was wel heel makkelijk?


def development_code():
    # Gebruik (delen van) deze code om je functies te testen tijdens het programmeren:
    stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
                'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert',
                'Roermond', 'Sittard', 'Maastricht']
    print(f"\n {stations} \n")
    beginstation = inlezen_beginstation(stations)
    eindstation = inlezen_eindstation(stations, beginstation)
    print(omroepen_reis(stations, beginstation, eindstation))


def module_runner():
    #development_code()  # Comment deze regel om je 'development_code' uit te schakelen
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


def __stations():
    return ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
            'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht']


def __out_of_input_error():
    raise AssertionError("Fout: er werd in de functie vaker om input gevraagd dan verwacht.")


def __check_testcase(simulated_input, function, function_args, expected_output):
    original_input = builtins.input
    simulated_input_copy = simulated_input.copy()
    simulated_input.reverse()
    builtins.input = lambda prompt="": simulated_input.pop() if len(simulated_input) > 0 else __out_of_input_error()

    try:
        __my_assert_args(function, function_args, expected_output)
    except AssertionError as ae:
        raise AssertionError(f"{ae.args[0]}\n -> Info: gesimuleerde input voor deze test: {simulated_input_copy}.") from ae
    finally:
        builtins.input = original_input


def test_inlezen_beginstation():
    function = inlezen_beginstation

    case = collections.namedtuple('case', 'simulated_input expected_start')
    testcases = [ case(["asfasf", "Schagen", "Alkmaar"], "Schagen"),
                  case(["Sittard" ], "Sittard"),
                  case(["Alkmr", "Alkmeer", "Alkmaar"], "Alkmaar") ]

    for test in testcases:
        __check_testcase(test.simulated_input, function, (__stations(),), test.expected_start)


def test_inlezen_eindstation():
    function = inlezen_eindstation

    case = collections.namedtuple('case', 'simulated_input start expected_stop')
    testcases = [ case(["asfasf", "Schagen", "Maastricht" ], "Schagen", "Maastricht"),
                  case(["asfsdf", "Schagen", "Alkmaar", "asfdfa", "Maastricht" ], "Alkmaar", "Maastricht"),
                  case(["Groningen", "Schagen", "Dedemsvaart", "Zaltbommel", "Eindhoven", "Den Briel" ], "Alkmaar", "Eindhoven")]

    for test in testcases:
        __check_testcase(test.simulated_input, function, (__stations(), test.start), test.expected_stop)


def test_omroepen_reis():
    function = omroepen_reis

    case = collections.namedtuple('case', 'start stop expected_start_rank, expected_transition_rank, expected_stop_rank, expected_distance expected_price')
    testcases = [ case("Schagen", "Maastricht", "1e station", "- Heerhugowaard\n- Alkmaar\n- Castricum\n- Zaandam\n- Amsterdam Sloterdijk\n- Amsterdam Centraal\n- Amsterdam Amstel\n- Utrecht Centraal\n- ’s-Hertogenbosch\n- Eindhoven\n- Weert\n- Roermond\n- Sittard", "15e station", "14 station", "70 euro"),
                  case("Alkmaar", "Weert", "3e station", "- Castricum\n- Zaandam\n- Amsterdam Sloterdijk\n- Amsterdam Centraal\n- Amsterdam Amstel\n- Utrecht Centraal\n- ’s-Hertogenbosch\n- Eindhoven", "12e station", "9 station", "45 euro"),
                  case("Heerhugowaard", "Sittard", "- Alkmaar\n- Castricum\n- Zaandam\n- Amsterdam Sloterdijk\n- Amsterdam Centraal\n- Amsterdam Amstel\n- Utrecht Centraal\n- ’s-Hertogenbosch\n- Eindhoven\n- Weert\n- Roermond\n", "2e station", "14e station", "12 station", "60 euro") ]


    for test in testcases:
        omroepbericht = function(__stations(), test.start, test.stop)
        assert type(omroepbericht) is str, f"Fout: omroepen_reis({__stations()}, {test.start}, {test.stop}) levert {type(omroepbericht).__name__} ipv string"

        assertmsg = f"Fout: omroepen_reis({__stations()}, {{}}, {{}}) bevat niet de vereiste {{}}-tekst '{{}}'. Jouw returnwaarde: \n<<\n"+omroepbericht+"\n>>"
        assert test.expected_start_rank in omroepbericht, assertmsg.format(test.start, test.stop, 'rangnummer-beginstation', test.expected_start_rank)
        assert test.expected_transition_rank in omroepbericht, assertmsg.format(test.start, test.stop, 'lijst met tussenstations:\n', test.expected_transition_rank)
        assert test.expected_stop_rank in omroepbericht, assertmsg.format(test.start, test.stop, 'rangnummer-eindstation', test.expected_stop_rank)
        assert test.expected_distance in omroepbericht, assertmsg.format(test.start, test.stop, 'afstand', test.expected_distance)
        assert test.expected_price in omroepbericht, assertmsg.format(test.start, test.stop, 'prijs', test.expected_price)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_inlezen_beginstation, test_inlezen_eindstation, test_omroepen_reis ]

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