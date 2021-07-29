{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6b59e96d",
   "metadata": {},
   "source": [
    "# Birthday Paradox Game"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "50b9af64",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime, random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1967508",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Birthday Paradox or Birthday Problem\n",
      "\n",
      "The Birthday Paradox show us the number of people, the odd\n",
      "that two of them have matching birthdays is surprisingly large.\n",
      "This program does a Monte Carlo simulation (that is, repeated random\n",
      "simulations) to explore this concept.\n",
      "\n",
      "(It's not actually a paradox, it's just a surprising result.)\n",
      "\n",
      "How many birthdays shall I generate? (Max 100)\n"
     ]
    }
   ],
   "source": [
    "def getBirthdays(numberOfBirthdays):\n",
    "    birthdays = []\n",
    "    \n",
    "    for i in range(numberOfBirthdays):\n",
    "        startOfYear = datetime.date(2001, 1, 1)\n",
    "        \n",
    "        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))\n",
    "        birthday = startOfYear + randomNumberOfDays\n",
    "        birthdays.append(birthday)\n",
    "    return birthdays\n",
    "\n",
    "def getMatch(birthdays):\n",
    "    if len(birthdays) == len(set(birthdays)):\n",
    "        return None \n",
    "    \n",
    "    for a, birthdayA in enumerate(birthdays):\n",
    "        for b, birthdayB in enumerate(birthdays[a + 1 :]):\n",
    "            if birthdayA == birthdayB:\n",
    "                return birthdayA\n",
    "#Displaying the intro\n",
    "print('''Birthday Paradox or Birthday Problem\n",
    "\n",
    "The Birthday Paradox show us the number of people, the odd\n",
    "that two of them have matching birthdays is surprisingly large.\n",
    "This program does a Monte Carlo simulation (that is, repeated random\n",
    "simulations) to explore this concept.\n",
    "\n",
    "(It's not actually a paradox, it's just a surprising result.)\n",
    "''')\n",
    "\n",
    "#A tuple which contains names of months in order:\n",
    "MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\n",
    "         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')\n",
    "\n",
    "while True:\n",
    "    print('How many birthdays shall I generate? (Max 100)')\n",
    "    response = input('>')\n",
    "    if response.isdecimal() and (0 < int(response) <= 100):\n",
    "        numBDays = int(response)\n",
    "        break\n",
    "print()\n",
    "\n",
    "print('Here are', numBDays, 'birthdays:')\n",
    "birthdays = getBirthdays(numBDays)\n",
    "\n",
    "for i, birthday in enumerate(birthdays):\n",
    "    if i != 0:\n",
    "        print(', ', end='')\n",
    "        monthName = MONTHS[birthday.month -1]\n",
    "        dateText = '{} {}'.format(monthName, birthday.day)\n",
    "        print(dateText, end='')\n",
    "print()\n",
    "print()\n",
    "\n",
    "match = getMatch(birthdays)\n",
    "\n",
    "#display the result\n",
    "\n",
    "print('In this simulation, ', end='')\n",
    "if match != None:\n",
    "    monthName = MONTHS[match.month - 1]\n",
    "    dateText = '{} {}'.format(monthName, match.day)\n",
    "    print('multiple people have a birthday on', dateText)\n",
    "else: \n",
    "    print('there are no matching birthdays.')\n",
    "print()\n",
    "\n",
    "print('Generating', numBDays, 'random birthdays 100,000 times...')\n",
    "input('Press Enter to begin...')\n",
    "\n",
    "\n",
    "print('Let\\'s run another 100,000 simulations.')\n",
    "simMatch = 0\n",
    "for i in range(100_000):\n",
    "    if i%10_000 == 0:\n",
    "        print(i, 'simulation run..')\n",
    "    birthdays = getBirthdays(numBDays)\n",
    "    if getMatch(birthdays) != None:\n",
    "        simMatch = simMatch + 1\n",
    "print('100,000 simulations run.')\n",
    "\n",
    "#display the simulation results:\n",
    "\n",
    "probability = round(simMatch / 100_000 * 100, 2)\n",
    "print('Out of 100,000 simulations of', numBDays, 'People, there was  a')\n",
    "print('Matching birthday in that group', simMatch, 'times. this means')\n",
    "print('having a matching birthday in their group.')\n",
    "print('that\\'s probably more than you would think!!')\n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ace714e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
