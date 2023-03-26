"""
.. module:: unit
    :platform: Linux, MacOS
    :synopsis: Explicitly expose the contents of openmm.unit for type hinting purposes

.. moduleauthor:: Charlles Abreu <craabreu@gmail.com>

"""

from openmm import unit as _unit

from .unit import *  # noqa: F401, F403

AVOGADRO_CONSTANT_NA = _unit.AVOGADRO_CONSTANT_NA
BOLTZMANN_CONSTANT_kB = _unit.BOLTZMANN_CONSTANT_kB
BaseDimension = _unit.BaseDimension
BaseUnit = _unit.BaseUnit
GRAVITATIONAL_CONSTANT_G = _unit.GRAVITATIONAL_CONSTANT_G
MOLAR_GAS_CONSTANT_R = _unit.MOLAR_GAS_CONSTANT_R
SPEED_OF_LIGHT_C = _unit.SPEED_OF_LIGHT_C
ScaledUnit = _unit.ScaledUnit
SiPrefix = _unit.SiPrefix
UnitSystem = _unit.UnitSystem
absolute_import = _unit.absolute_import
acos = _unit.acos
acosh = _unit.acosh
amount_dimension = _unit.amount_dimension
amp = _unit.amp
ampere = _unit.ampere
amperes = _unit.amperes
amps = _unit.amps
amu = _unit.amu
amus = _unit.amus
angle_dimension = _unit.angle_dimension
angstrom = _unit.angstrom
angstroms = _unit.angstroms
arcminute = _unit.arcminute
arcminutes = _unit.arcminutes
arcsecond = _unit.arcsecond
arcseconds = _unit.arcseconds
asin = _unit.asin
asinh = _unit.asinh
atan = _unit.atan
atan2 = _unit.atan2
atanh = _unit.atanh
atmosphere = _unit.atmosphere
atmospheres = _unit.atmospheres
atom_mass_units = _unit.atom_mass_units
atomic_mass_unit = _unit.atomic_mass_unit
atto = _unit.atto
attocalorie = _unit.attocalorie
attocalories = _unit.attocalories
attogram = _unit.attogram
attograms = _unit.attograms
attojoule = _unit.attojoule
attojoules = _unit.attojoules
attoliter = _unit.attoliter
attoliters = _unit.attoliters
attometer = _unit.attometer
attometers = _unit.attometers
attomolar = _unit.attomolar
attomolars = _unit.attomolars
attonewton = _unit.attonewton
attonewtons = _unit.attonewtons
attopascal = _unit.attopascal
attopascals = _unit.attopascals
attosecond = _unit.attosecond
attoseconds = _unit.attoseconds
ban = _unit.ban
bans = _unit.bans
bar = _unit.bar  # pylint: disable=disallowed-name
bars = _unit.bars
basedimension = _unit.basedimension
baseunit = _unit.baseunit
binary_prefixes = _unit.binary_prefixes
bit = _unit.bit
bits = _unit.bits
bohr = _unit.bohr
bohrs = _unit.bohrs
byte = _unit.byte
bytes = _unit.bytes  # pylint: disable=redefined-builtin
calorie = _unit.calorie
calories = _unit.calories
candela = _unit.candela
candelas = _unit.candelas
centi = _unit.centi
centicalorie = _unit.centicalorie
centicalories = _unit.centicalories
centigram = _unit.centigram
centigrams = _unit.centigrams
centijoule = _unit.centijoule
centijoules = _unit.centijoules
centiliter = _unit.centiliter
centiliters = _unit.centiliters
centimeter = _unit.centimeter
centimeters = _unit.centimeters
centimolar = _unit.centimolar
centimolars = _unit.centimolars
centinewton = _unit.centinewton
centinewtons = _unit.centinewtons
centipascal = _unit.centipascal
centipascals = _unit.centipascals
centisecond = _unit.centisecond
centiseconds = _unit.centiseconds
centuries = _unit.centuries
century = _unit.century
centurys = _unit.centurys
cgs_unit_system = _unit.cgs_unit_system
charge_dimension = _unit.charge_dimension
constants = _unit.constants
cos = _unit.cos
cosh = _unit.cosh
coulomb = _unit.coulomb
coulombs = _unit.coulombs
dalton = _unit.dalton
daltons = _unit.daltons
day = _unit.day
days = _unit.days
debye = _unit.debye
debyes = _unit.debyes
deca = _unit.deca
decacalorie = _unit.decacalorie
decacalories = _unit.decacalories
decagram = _unit.decagram
decagrams = _unit.decagrams
decajoule = _unit.decajoule
decajoules = _unit.decajoules
decaliter = _unit.decaliter
decaliters = _unit.decaliters
decameter = _unit.decameter
decameters = _unit.decameters
decamolar = _unit.decamolar
decamolars = _unit.decamolars
decanewton = _unit.decanewton
decanewtons = _unit.decanewtons
decapascal = _unit.decapascal
decapascals = _unit.decapascals
decasecond = _unit.decasecond
decaseconds = _unit.decaseconds
deci = _unit.deci
decicalorie = _unit.decicalorie
decicalories = _unit.decicalories
decigram = _unit.decigram
decigrams = _unit.decigrams
decijoule = _unit.decijoule
decijoules = _unit.decijoules
deciliter = _unit.deciliter
deciliters = _unit.deciliters
decimeter = _unit.decimeter
decimeters = _unit.decimeters
decimolar = _unit.decimolar
decimolars = _unit.decimolars
decinewton = _unit.decinewton
decinewtons = _unit.decinewtons
decipascal = _unit.decipascal
decipascals = _unit.decipascals
decisecond = _unit.decisecond
deciseconds = _unit.deciseconds
define_prefixed_units = _unit.define_prefixed_units
degree = _unit.degree
degrees = _unit.degrees
deka = _unit.deka
dekacalorie = _unit.dekacalorie
dekacalories = _unit.dekacalories
dekagram = _unit.dekagram
dekagrams = _unit.dekagrams
dekajoule = _unit.dekajoule
dekajoules = _unit.dekajoules
dekaliter = _unit.dekaliter
dekaliters = _unit.dekaliters
dekameter = _unit.dekameter
dekameters = _unit.dekameters
dekamolar = _unit.dekamolar
dekamolars = _unit.dekamolars
dekanewton = _unit.dekanewton
dekanewtons = _unit.dekanewtons
dekapascal = _unit.dekapascal
dekapascals = _unit.dekapascals
dekasecond = _unit.dekasecond
dekaseconds = _unit.dekaseconds
dimensionless = _unit.dimensionless
dit = _unit.dit
dits = _unit.dits
division = _unit.division
dot = _unit.dot
dyne = _unit.dyne
dynes = _unit.dynes
elementary_charge = _unit.elementary_charge
elementary_charges = _unit.elementary_charges
erg = _unit.erg
ergs = _unit.ergs
exa = _unit.exa
exacalorie = _unit.exacalorie
exacalories = _unit.exacalories
exagram = _unit.exagram
exagrams = _unit.exagrams
exajoule = _unit.exajoule
exajoules = _unit.exajoules
exaliter = _unit.exaliter
exaliters = _unit.exaliters
exameter = _unit.exameter
exameters = _unit.exameters
examolar = _unit.examolar
examolars = _unit.examolars
exanewton = _unit.exanewton
exanewtons = _unit.exanewtons
exapascal = _unit.exapascal
exapascals = _unit.exapascals
exasecond = _unit.exasecond
exaseconds = _unit.exaseconds
exbi = _unit.exbi
farad = _unit.farad
farads = _unit.farads
feet = _unit.feet
femto = _unit.femto
femtocalorie = _unit.femtocalorie
femtocalories = _unit.femtocalories
femtogram = _unit.femtogram
femtograms = _unit.femtograms
femtojoule = _unit.femtojoule
femtojoules = _unit.femtojoules
femtoliter = _unit.femtoliter
femtoliters = _unit.femtoliters
femtometer = _unit.femtometer
femtometers = _unit.femtometers
femtomolar = _unit.femtomolar
femtomolars = _unit.femtomolars
femtonewton = _unit.femtonewton
femtonewtons = _unit.femtonewtons
femtopascal = _unit.femtopascal
femtopascals = _unit.femtopascals
femtosecond = _unit.femtosecond
femtoseconds = _unit.femtoseconds
foot = _unit.foot
fortnight = _unit.fortnight
fortnights = _unit.fortnights
furlong = _unit.furlong
furlongs = _unit.furlongs
gauss = _unit.gauss
gibi = _unit.gibi
giga = _unit.giga
gigacalorie = _unit.gigacalorie
gigacalories = _unit.gigacalories
gigagram = _unit.gigagram
gigagrams = _unit.gigagrams
gigajoule = _unit.gigajoule
gigajoules = _unit.gigajoules
gigaliter = _unit.gigaliter
gigaliters = _unit.gigaliters
gigameter = _unit.gigameter
gigameters = _unit.gigameters
gigamolar = _unit.gigamolar
gigamolars = _unit.gigamolars
giganewton = _unit.giganewton
giganewtons = _unit.giganewtons
gigapascal = _unit.gigapascal
gigapascals = _unit.gigapascals
gigasecond = _unit.gigasecond
gigaseconds = _unit.gigaseconds
gram = _unit.gram
grams = _unit.grams
hartley = _unit.hartley
hartleys = _unit.hartleys
hartree = _unit.hartree
hartrees = _unit.hartrees
hecto = _unit.hecto
hectocalorie = _unit.hectocalorie
hectocalories = _unit.hectocalories
hectogram = _unit.hectogram
hectograms = _unit.hectograms
hectojoule = _unit.hectojoule
hectojoules = _unit.hectojoules
hectoliter = _unit.hectoliter
hectoliters = _unit.hectoliters
hectometer = _unit.hectometer
hectometers = _unit.hectometers
hectomolar = _unit.hectomolar
hectomolars = _unit.hectomolars
hectonewton = _unit.hectonewton
hectonewtons = _unit.hectonewtons
hectopascal = _unit.hectopascal
hectopascals = _unit.hectopascals
hectosecond = _unit.hectosecond
hectoseconds = _unit.hectoseconds
henries = _unit.henries
henry = _unit.henry
henrys = _unit.henrys
hour = _unit.hour
hours = _unit.hours
inch = _unit.inch
inches = _unit.inches
information_dimension = _unit.information_dimension
is_quantity = _unit.is_quantity
is_unit = _unit.is_unit
item = _unit.item
items = _unit.items
joule = _unit.joule
joules = _unit.joules
kelvin = _unit.kelvin
kelvins = _unit.kelvins
kibi = _unit.kibi
kilo = _unit.kilo
kilocalorie = _unit.kilocalorie
kilocalorie_per_mole = _unit.kilocalorie_per_mole
kilocalories = _unit.kilocalories
kilocalories_per_mole = _unit.kilocalories_per_mole
kilogram = _unit.kilogram
kilograms = _unit.kilograms
kilojoule = _unit.kilojoule
kilojoule_per_mole = _unit.kilojoule_per_mole
kilojoules = _unit.kilojoules
kilojoules_per_mole = _unit.kilojoules_per_mole
kiloliter = _unit.kiloliter
kiloliters = _unit.kiloliters
kilometer = _unit.kilometer
kilometers = _unit.kilometers
kilomolar = _unit.kilomolar
kilomolars = _unit.kilomolars
kilonewton = _unit.kilonewton
kilonewtons = _unit.kilonewtons
kilopascal = _unit.kilopascal
kilopascals = _unit.kilopascals
kilosecond = _unit.kilosecond
kiloseconds = _unit.kiloseconds
length_dimension = _unit.length_dimension
liter = _unit.liter
liters = _unit.liters
litre = _unit.litre
litres = _unit.litres
luminous_intensity_dimension = _unit.luminous_intensity_dimension
mass_dimension = _unit.mass_dimension
math = _unit.math
md_kilocalorie = _unit.md_kilocalorie
md_kilocalories = _unit.md_kilocalories
md_kilojoule = _unit.md_kilojoule
md_kilojoule_raw = _unit.md_kilojoule_raw
md_kilojoules = _unit.md_kilojoules
md_unit_system = _unit.md_unit_system
mebi = _unit.mebi
mega = _unit.mega
megacalorie = _unit.megacalorie
megacalories = _unit.megacalories
megagram = _unit.megagram
megagrams = _unit.megagrams
megajoule = _unit.megajoule
megajoules = _unit.megajoules
megaliter = _unit.megaliter
megaliters = _unit.megaliters
megameter = _unit.megameter
megameters = _unit.megameters
megamolar = _unit.megamolar
megamolars = _unit.megamolars
meganewton = _unit.meganewton
meganewtons = _unit.meganewtons
megapascal = _unit.megapascal
megapascals = _unit.megapascals
megasecond = _unit.megasecond
megaseconds = _unit.megaseconds
meter = _unit.meter
meters = _unit.meters
micro = _unit.micro
microcalorie = _unit.microcalorie
microcalories = _unit.microcalories
microgram = _unit.microgram
micrograms = _unit.micrograms
microjoule = _unit.microjoule
microjoules = _unit.microjoules
microliter = _unit.microliter
microliters = _unit.microliters
micrometer = _unit.micrometer
micrometers = _unit.micrometers
micromolar = _unit.micromolar
micromolars = _unit.micromolars
micronewton = _unit.micronewton
micronewtons = _unit.micronewtons
micropascal = _unit.micropascal
micropascals = _unit.micropascals
microsecond = _unit.microsecond
microseconds = _unit.microseconds
mile = _unit.mile
miles = _unit.miles
millenia = _unit.millenia
millenium = _unit.millenium
milleniums = _unit.milleniums
milli = _unit.milli
millicalorie = _unit.millicalorie
millicalories = _unit.millicalories
milligram = _unit.milligram
milligrams = _unit.milligrams
millijoule = _unit.millijoule
millijoules = _unit.millijoules
milliliter = _unit.milliliter
milliliters = _unit.milliliters
millimeter = _unit.millimeter
millimeters = _unit.millimeters
millimolar = _unit.millimolar
millimolars = _unit.millimolars
millinewton = _unit.millinewton
millinewtons = _unit.millinewtons
millipascal = _unit.millipascal
millipascals = _unit.millipascals
millisecond = _unit.millisecond
milliseconds = _unit.milliseconds
minute = _unit.minute
minutes = _unit.minutes
mmHg = _unit.mmHg
molal = _unit.molal
molar = _unit.molar
mole = _unit.mole
moles = _unit.moles
mymatrix = _unit.mymatrix
nano = _unit.nano
nanocalorie = _unit.nanocalorie
nanocalories = _unit.nanocalories
nanogram = _unit.nanogram
nanograms = _unit.nanograms
nanojoule = _unit.nanojoule
nanojoules = _unit.nanojoules
nanoliter = _unit.nanoliter
nanoliters = _unit.nanoliters
nanometer = _unit.nanometer
nanometers = _unit.nanometers
nanomolar = _unit.nanomolar
nanomolars = _unit.nanomolars
nanonewton = _unit.nanonewton
nanonewtons = _unit.nanonewtons
nanopascal = _unit.nanopascal
nanopascals = _unit.nanopascals
nanosecond = _unit.nanosecond
nanoseconds = _unit.nanoseconds
nat = _unit.nat
nats = _unit.nats
nepit = _unit.nepit
nepits = _unit.nepits
newton = _unit.newton
newtons = _unit.newtons
nit = _unit.nit
nits = _unit.nits
norm = _unit.norm
ohm = _unit.ohm
ohms = _unit.ohms
pascal = _unit.pascal
pascals = _unit.pascals
pebi = _unit.pebi
peta = _unit.peta
petacalorie = _unit.petacalorie
petacalories = _unit.petacalories
petagram = _unit.petagram
petagrams = _unit.petagrams
petajoule = _unit.petajoule
petajoules = _unit.petajoules
petaliter = _unit.petaliter
petaliters = _unit.petaliters
petameter = _unit.petameter
petameters = _unit.petameters
petamolar = _unit.petamolar
petamolars = _unit.petamolars
petanewton = _unit.petanewton
petanewtons = _unit.petanewtons
petapascal = _unit.petapascal
petapascals = _unit.petapascals
petasecond = _unit.petasecond
petaseconds = _unit.petaseconds
pico = _unit.pico
picocalorie = _unit.picocalorie
picocalories = _unit.picocalories
picogram = _unit.picogram
picograms = _unit.picograms
picojoule = _unit.picojoule
picojoules = _unit.picojoules
picoliter = _unit.picoliter
picoliters = _unit.picoliters
picometer = _unit.picometer
picometers = _unit.picometers
picomolar = _unit.picomolar
picomolars = _unit.picomolars
piconewton = _unit.piconewton
piconewtons = _unit.piconewtons
picopascal = _unit.picopascal
picopascals = _unit.picopascals
picosecond = _unit.picosecond
picoseconds = _unit.picoseconds
planck_unit_system = _unit.planck_unit_system
pound_force = _unit.pound_force
pound_mass = _unit.pound_mass
pounds_force = _unit.pounds_force
pounds_mass = _unit.pounds_mass
prefix = _unit.prefix
print_function = _unit.print_function
psi = _unit.psi
quantity = _unit.quantity
radian = _unit.radian
radians = _unit.radians
second = _unit.second
seconds = _unit.seconds
si_prefixes = _unit.si_prefixes
si_unit_system = _unit.si_unit_system
sin = _unit.sin
sinh = _unit.sinh
sqrt = _unit.sqrt
standard_dimensions = _unit.standard_dimensions
stone = _unit.stone
stones = _unit.stones
sum = _unit.sum  # pylint: disable=redefined-builtin
sys = _unit.sys
tan = _unit.tan
tanh = _unit.tanh
tebi = _unit.tebi
temperature_dimension = _unit.temperature_dimension
tera = _unit.tera
teracalorie = _unit.teracalorie
teracalories = _unit.teracalories
teragram = _unit.teragram
teragrams = _unit.teragrams
terajoule = _unit.terajoule
terajoules = _unit.terajoules
teraliter = _unit.teraliter
teraliters = _unit.teraliters
terameter = _unit.terameter
terameters = _unit.terameters
teramolar = _unit.teramolar
teramolars = _unit.teramolars
teranewton = _unit.teranewton
teranewtons = _unit.teranewtons
terapascal = _unit.terapascal
terapascals = _unit.terapascals
terasecond = _unit.terasecond
teraseconds = _unit.teraseconds
tesla = _unit.tesla
teslas = _unit.teslas
time_dimension = _unit.time_dimension
torr = _unit.torr
unit = _unit.unit
unit_definitions = _unit.unit_definitions
unit_math = _unit.unit_math
unit_operators = _unit.unit_operators
volt = _unit.volt
volts = _unit.volts
watt = _unit.watt
watts = _unit.watts
week = _unit.week
weeks = _unit.weeks
yard = _unit.yard
yards = _unit.yards
year = _unit.year
years = _unit.years
yobi = _unit.yobi
yotta = _unit.yotta
yottacalorie = _unit.yottacalorie
yottacalories = _unit.yottacalories
yottagram = _unit.yottagram
yottagrams = _unit.yottagrams
yottajoule = _unit.yottajoule
yottajoules = _unit.yottajoules
yottaliter = _unit.yottaliter
yottaliters = _unit.yottaliters
yottameter = _unit.yottameter
yottameters = _unit.yottameters
yottamolar = _unit.yottamolar
yottamolars = _unit.yottamolars
yottanewton = _unit.yottanewton
yottanewtons = _unit.yottanewtons
yottapascal = _unit.yottapascal
yottapascals = _unit.yottapascals
yottasecond = _unit.yottasecond
yottaseconds = _unit.yottaseconds
yotto = _unit.yotto
yottocalorie = _unit.yottocalorie
yottocalories = _unit.yottocalories
yottogram = _unit.yottogram
yottograms = _unit.yottograms
yottojoule = _unit.yottojoule
yottojoules = _unit.yottojoules
yottoliter = _unit.yottoliter
yottoliters = _unit.yottoliters
yottometer = _unit.yottometer
yottometers = _unit.yottometers
yottomolar = _unit.yottomolar
yottomolars = _unit.yottomolars
yottonewton = _unit.yottonewton
yottonewtons = _unit.yottonewtons
yottopascal = _unit.yottopascal
yottopascals = _unit.yottopascals
yottosecond = _unit.yottosecond
yottoseconds = _unit.yottoseconds
zebi = _unit.zebi
zepto = _unit.zepto
zeptocalorie = _unit.zeptocalorie
zeptocalories = _unit.zeptocalories
zeptogram = _unit.zeptogram
zeptograms = _unit.zeptograms
zeptojoule = _unit.zeptojoule
zeptojoules = _unit.zeptojoules
zeptoliter = _unit.zeptoliter
zeptoliters = _unit.zeptoliters
zeptometer = _unit.zeptometer
zeptometers = _unit.zeptometers
zeptomolar = _unit.zeptomolar
zeptomolars = _unit.zeptomolars
zeptonewton = _unit.zeptonewton
zeptonewtons = _unit.zeptonewtons
zeptopascal = _unit.zeptopascal
zeptopascals = _unit.zeptopascals
zeptosecond = _unit.zeptosecond
zeptoseconds = _unit.zeptoseconds
zetta = _unit.zetta
zettacalorie = _unit.zettacalorie
zettacalories = _unit.zettacalories
zettagram = _unit.zettagram
zettagrams = _unit.zettagrams
zettajoule = _unit.zettajoule
zettajoules = _unit.zettajoules
zettaliter = _unit.zettaliter
zettaliters = _unit.zettaliters
zettameter = _unit.zettameter
zettameters = _unit.zettameters
zettamolar = _unit.zettamolar
zettamolars = _unit.zettamolars
zettanewton = _unit.zettanewton
zettanewtons = _unit.zettanewtons
zettapascal = _unit.zettapascal
zettapascals = _unit.zettapascals
zettasecond = _unit.zettasecond
zettaseconds = _unit.zettaseconds
