import json
import pprint

JSON_OLD = {
    "company_id": 111111,
    "resource": "record",
    "resource_id": 406155061,
    "status": "create",
    "data": {
        "id": 11111111,
        "company_id": 111111,
        "services": [
            {
                "id": 9035445,
                "title": "Стрижка",
                "cost": 1500,
                "cost_per_unit": 1500,
                "first_cost": 1500,
                "amount": 1,
            }
        ],
        "goods_transactions": [],
        "staff": {"id": 1819441, "name": "Мастер"},
        "client": {
            "id": 130345867,
            "name": "Клиент",
            "phone": "79111111111",
            "success_visits_count": 2,
            "fail_visits_count": 0,
        },
        "clients_count": 1,
        "datetime": "2022-01-25T11:00:00+03:00",
        "create_date": "2022-01-22T00:54:00+03:00",
        "online": False,
        "attendance": 0,
        "confirmed": 1,
        "seance_length": 3600,
        "length": 3600,
        "master_request": 1,
        "visit_id": 346427049,
        "created_user_id": 10573443,
        "deleted": False,
        "paid_full": 0,
        "last_change_date": "2022-01-22T00:54:00+03:00",
        "record_labels": "",
        "date": "2022-01-22 10:00:00",
    },
}
JSON_NEW = {
    "company_id": 111111,
    "resource": "record",
    "resource_id": 406155061,
    "status": "create",
    "data": {
        "id": 11111111,
        "company_id": 111111,
        "services": [
            {
                "id": 22222225,
                "title": "Стрижка",
                "cost": 1500,
                "cost_per_unit": 1500,
                "first_cost": 1500,
                "amount": 1,
            }
        ],
        "goods_transactions": [],
        "staff": {"id": 1819441, "name": "Мастер"},
        "client": {
            "id": 130345867,
            "name": "Клиент",
            "phone": "79111111111",
            "success_visits_count": 2,
            "fail_visits_count": 0,
        },
        "clients_count": 1,
        "datetime": "2022-01-25T13:00:00+03:00",
        "create_date": "2022-01-22T00:54:00+03:00",
        "online": False,
        "attendance": 2,
        "confirmed": 1,
        "seance_length": 3600,
        "length": 3600,
        "master_request": 1,
        "visit_id": 346427049,
        "created_user_id": 10573443,
        "deleted": False,
        "paid_full": 1,
        "last_change_date": "2022-01-22T00:54:00+03:00",
        "record_labels": "",
        "date": "2022-01-22 10:00:00",
    },
}


class JsonChecker:

    diff_list = ["services", "staff", "datetime"]

    def check(self, old_data: dict, new_data: dict) -> dict | None:
        if json.dumps(old_data) == json.dumps(new_data):
            print("All data equal")
            return
        changes = {}
        for k in self.diff_list:
            k_in_old = next(self._find_key(old_data, k))
            k_in_new = next(self._find_key(new_data, k))
            if k_in_old != k_in_new:
                changes[k] = k_in_new[-1]
        return changes

    def _find_key(self, obj, key):
        if isinstance(obj, dict):
            yield from self._iter_dict(obj, key, [])
        elif isinstance(obj, list):
            yield from self._iter_list(obj, key, [])

    def _iter_dict(self, d, key, indices):
        for k, v in d.items():
            if k == key:
                yield indices + [k], v
            if isinstance(v, dict):
                yield from self._iter_dict(v, key, indices + [k])
            elif isinstance(v, list):
                yield from self._iter_list(v, key, indices + [k])

    def _iter_list(self, seq, key, indices):
        for k, v in enumerate(seq):
            if isinstance(v, dict):
                yield from self._iter_dict(v, key, indices + [k])
            elif isinstance(v, list):
                yield from self._iter_list(v, key, indices + [k])


if __name__ == "__main__":
    checker = JsonChecker()
    print("=" * 25, "Testing with differences", "=" * 25)
    pprint.pprint(checker.check(JSON_OLD, JSON_NEW))
    print("=" * 25, "Testing without differences", "=" * 25)
    checker.check(JSON_OLD, JSON_OLD)
