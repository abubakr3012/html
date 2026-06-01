__new__	ClassName(...)	Сохтани объекти нав (пеш аз __init__)	Объект
__init__	ClassName(...)	Инициализатсияи объект — конструктор	Объект
__del__	del obj	Нест кардани объект — деструктор	Объект
__repr__	repr(obj)	Намоиши расмии объект барои debugging	Объект
__str__	print(obj), str(obj)	Намоиши матнии объект барои корбар	Объект
__bytes__	bytes(obj)	Табдил ба байт	Объект
__format__	format(obj), f-string	Форматкунии муфассал	Объект
__hash__	hash(obj), dict key	Ҳисоби хеши объект	Объект
__bool__	bool(obj), if obj:	Арзиши мантиқии объект	Объект
__sizeof__	sys.getsizeof(obj)	Андозаи хотира (байт)	Объект
__eq__	obj == other	Баробарии ду объект	Муқоиса
__ne__	obj != other	Нобаробарии ду объект	Муқоиса
__lt__	obj < other	Камтар будан	Муқоиса
__le__	obj <= other	Камтар ё баробар будан	Муқоиса
__gt__	obj > other	Бузургтар будан	Муқоиса
__ge__	obj >= other	Бузургтар ё баробар будан	Муқоиса
__add__	obj + other	Ҷамъ	Рақамӣ
__radd__	other + obj	Ҷамъи ростгард (obj дар тарафи рост)	Рақамӣ
__iadd__	obj += other	Ҷамъи дохилӣ (augmented assignment)	Рақамӣ
__sub__	obj - other	Тарҳ	Рақамӣ
__mul__	obj * other	Зарб	Рақамӣ
__truediv__	obj / other	Тақсим	Рақамӣ
__floordiv__	obj // other	Тақсими бутун	Рақамӣ
__mod__	obj % other	Боқимонда аз тақсим	Рақамӣ
__pow__	obj ** other	Дараҷа	Рақамӣ
__neg__	-obj	Унарии манфӣ	Рақамӣ
__pos__	+obj	Унарии мусбат	Рақамӣ
__abs__	abs(obj)	Қимати мутлақ	Рақамӣ
__round__	round(obj)	Дурустгирӣ	Рақамӣ
__int__	int(obj)	Табдил ба бутун	Рақамӣ
__float__	float(obj)	Табдил ба дуҷина	Рақамӣ
__complex__	complex(obj)	Табдил ба мураккаб	Рақамӣ
__index__	list[obj]	Табдили ба индекс (ҳатман int)	Рақамӣ
__and__	obj & other	AND-и битӣ	Рақамӣ
__or__	obj | other	OR-и битӣ	Рақамӣ
__xor__	obj ^ other	XOR-и битӣ	Рақамӣ
__lshift__	obj << other	Сурати чап	Рақамӣ
__rshift__	obj >> other	Сурати рост	Рақамӣ
__len__	len(obj)	Дарозии объект	Контейнер
__getitem__	obj[key]	Гирифтани элемент бо калид/индекс	Контейнер
__setitem__	obj[key] = val	Гузоштани элемент	Контейнер
__delitem__	del obj[key]	Нест кардани элемент	Контейнер
__contains__	x in obj	Тафтиши мавҷудияти элемент	Контейнер
__missing__	dict[missing_key]	Рафтор ҳангоми калиди нест (дар dict)	Контейнер
__reversed__	reversed(obj)	Итераторе барои тартиби баръакс	Контейнер
__iter__	for x in obj, iter(obj)	Итераторро бармегардонад	Итератсия
__next__	next(obj)	Элементи оянда	Итератсия
__getattr__	obj.missing_attr	Аттрибути ёфтнашударо идора мекунад	Аттрибут
__getattribute__	obj.any_attr	Ҳар дастрасӣ ба аттрибут	Аттрибут
__setattr__	obj.attr = val	Гузоштани аттрибут	Аттрибут
__delattr__	del obj.attr	Нест кардани аттрибут	Аттрибут
__dir__	dir(obj)	Рӯйхати аттрибутҳо	Аттрибут
__enter__	with obj as x:	Вуруд ба блоки with	Контекст
__exit__	Охири блоки with	Хуруҷ аз with (иштибоҳро идора мекунад)	Контекст
__class_getitem__	Class[int]	Дастгирии дженерикҳо (typing)	Строк
__init_subclass__	class B(A):	Ҳангоми мерос гирифтан аз синф фаъол мешавад	Строк
__set_name__	class-level descriptor	Ҳангоми таъин кардани дескриптор	Строк
__await__	await obj	Объектро awaitable месозад	Async
__aiter__	async for x in obj:	Итератори асинхронӣ	Async
__anext__	async for, await next()	Элементи оянда дар async итератсия	Async
__aenter__	async with obj:	Вуруди асинхронӣ ба with	Async
__aexit__	async with (охир)	Хуруҷи асинхронӣ аз with	Async
__get__	obj.descriptor	Гирифтани дескриптор	Строк
__set__	obj.descriptor = val	Гузоштани дескриптор	Строк
__delete__	del obj.descriptor	Нест кардани дескриптор	Строк
__call__	obj()	Объектро чун функсия фаъол месозад	Объект
__copy__	copy.copy(obj)	Нусхабардории сатҳӣ	Объект
__deepcopy__	copy.deepcopy(obj)	Нусхабардории чуқур	Объект
__reduce__	pickle.dumps(obj)	Сериализатсия (pickle)	Объект
__getstate__	pickle.dumps(obj)	Гирифтани ҳолат ҳангоми pickle	Объект
__setstate__	pickle.loads(data)	Барқарор кардани ҳолат аз pickle	