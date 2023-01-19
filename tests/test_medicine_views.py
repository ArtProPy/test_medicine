import json

from django.test import TransactionTestCase

import tests.data_factories as df
from medicine.models import Reference, VersionReference, ElementReference


class TestReferenceViewSet(TransactionTestCase):
    BASE_URL = '/refbooks'

    @classmethod
    def setUp(cls) -> None:
        with open(f'tests/stubs/medicine.json', 'r', encoding='utf-8') as file:
            cls.test_data = json.loads(''.join(file.readlines()).replace('\n', ''))

    def test_refbooks_list(self):
        """
        Проверяет логику получения списка справочников.

        Тесты:
        - Вернуть список справочников, если БД пуста;
        - Вернуть список справочников, если в БД есть только один справочник;
        - Вернуть список справочников, если в БД есть несколько справочников;
        - Вернуть список справочников с указаной датой версии, если в БД нет соответствующих справочников;
        - Вернуть список справочников с указаной датой версии при наличии в БД соответствующих справочников;
        - Вернуть список идентификаторов справочников с указаной датой версии при наличии в БД
        соответствующих справочников;
        - Вернуть список названий справочников с указаной датой версии при наличии в БД соответствующих справочников.
        """

        for subtest_data in self.test_data[self._testMethodName]:
            with self.subTest(subtest_data['name']):
                for reference in subtest_data['references']:
                    df.ReferenceFactory(id=reference['id'], name=reference['name'], code=reference['code'])

                for version in subtest_data['versions']:
                    df.VersionReferenceFactory(date=version['date'], reference_id=version['ref'], version=version['v'])

                url = self.BASE_URL
                url += '.id' if subtest_data['only_id'] else ''
                url += '.name' if subtest_data['only_name'] else ''

                params = {'date': subtest_data['date']} if subtest_data['date'] else {}

                responce = self.client.get(url + '/', data=params, format='json')

                self.assertEqual(responce.status_code, 200)
                self.assertIsNotNone(responce.data.get('refbooks'))
                self.assertCountEqual(responce.data['refbooks'], subtest_data['currect_result'])

                Reference.objects.all().delete()
                VersionReference.objects.all().delete()


class TestElementReferenceViewSet(TransactionTestCase):
    BASE_URL = '/refbooks'

    @classmethod
    def setUp(cls) -> None:
        with open(f'tests/stubs/medicine.json', 'r', encoding='utf-8') as file:
            cls.test_data = json.loads(''.join(file.readlines()).replace('\n', ''))

    def test_elements_list(self):
        """
        Проверяет логику получения списка элементов справочников.

        Тесты:
        - Вернуть список элементов, если БД пуста;
        - Вернуть список элементов, если в БД есть только элементы другого справочника;
        - Вернуть список элементов, если в БД есть соответствующие элементы справочника;
        - Вернуть список кодов элементов, если в БД есть соответствующие элементы справочника;
        - Вернуть список значений элементов, если в БД есть соответствующие элементы справочника;
        - Вернуть список значений элементов, если указана версия, соответствующей которой нет у указанного справочника;
        - Вернуть список значений элементов, если указана существующая версия справочника.
        """

        for num in range(1, 3):
            df.ReferenceFactory(id=num)
        for subtest_data in self.test_data[self._testMethodName]:
            with self.subTest(subtest_data['name']):
                for version in subtest_data['versions']:
                    df.VersionReferenceFactory(
                        id=version['id'], date=version['date'], reference_id=version['ref'], version=version['v']
                    )

                for element in subtest_data['elements']:
                    df.ElementReferenceFactory(
                        version_reference_id=element['v_id'], code=element['code'], value=element['value']
                    )

                url = f'{self.BASE_URL}/1/elements'
                url += '.code' if subtest_data['only_code'] else ''
                url += '.value' if subtest_data['only_value'] else ''

                params = {'version': subtest_data['version']} if subtest_data['version'] else {}

                responce = self.client.get(url + '/', data=params, format='json')

                self.assertEqual(responce.status_code, 200)
                self.assertIsNotNone(responce.data.get('elements'))
                self.assertCountEqual(responce.data['elements'], subtest_data['currect_result'])

                VersionReference.objects.all().delete()
                ElementReference.objects.all().delete()
