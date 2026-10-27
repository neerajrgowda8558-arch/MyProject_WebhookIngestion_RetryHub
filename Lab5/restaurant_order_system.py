
"""Restaurant dining order billing and kitchen ticket module."""

import hashlib
import json
import secrets

ORDERS = {
    "T1": {
        "guest": "Liam",
        "items": 3,
        "bill": 45.0,
        "is_settled": False,
    },
    "T2": {
        "guest": "Sophia",
        "items": 1,
        "bill": 18.0,
        "is_settled": True,
    },
    "T3": {
        "guest": "Mason",
        "items": 4,
        "bill": 72.0,
        "is_settled": False,
    },
}

ITEM_PRICE = 15.0
KITCHEN_ORDERS_FILE = "kitchen_orders.txt"


def place_table_order(
    table_id, guest, items_count, order_log=None
):
    """Create a new table order and record it in the order log."""
    if table_id in ORDERS or items_count <= 0:
        return False

    ORDERS[table_id] = {
        "guest": guest,
        "items": items_count,
        "bill": ITEM_PRICE * items_count,
        "is_settled": False,
    }

    if order_log is not None:
        order_log.append(
            f"Created order for {table_id} "
            f"with {items_count} dishes"
        )

    return True


def void_table_order(table_id):
    """Remove an existing table order."""
    if table_id not in ORDERS:
        return False

    del ORDERS[table_id]
    return True


def check_table_status(table_id):
    """Return whether an existing order is awaiting payment."""
    order = ORDERS.get(table_id)

    if order is None:
        return False

    return not order["is_settled"]


def calculate_discounted_bill(table_id, discount_rate=0.10):
    """Calculate a discounted bill using a validated discount rate."""
    if table_id not in ORDERS:
        raise KeyError(f"Unknown table ID: {table_id}")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    base_bill = ORDERS[table_id]["bill"]
    return round(base_bill * (1 - discount_rate), 2)


def generate_ticket_hash(table_id):
    """Generate a SHA-256 digest for a table ticket identifier."""
    return hashlib.sha256(table_id.encode("utf-8")).hexdigest()


def generate_pos_pin():
    """Generate a cryptographically secure four-digit PIN."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_kitchen_orders(filename=KITCHEN_ORDERS_FILE):
    """Write current orders to a kitchen ticket file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(ORDERS, file, indent=4)

    print(f"Ticket sent to kitchen printer: {filename}")


def get_pending_summary(order_data):
    """Count orders that have not yet been settled."""
    return sum(
        not details["is_settled"]
        for details in order_data.values()
    )


def main():
    """Execute sample restaurant billing operations."""
    place_table_order("T4", "Olivia", 2)
    void_table_order("T2")

    print("Is T1 pending:", check_table_status("T1"))
    print(
        "Discounted Bill:",
        calculate_discounted_bill("T1", 0.10),
    )
    print("Ticket Hash:", generate_ticket_hash("T1"))
    print("POS PIN:", generate_pos_pin())

    export_kitchen_orders()
    print("Pending tables:", get_pending_summary(ORDERS))


if __name__ == "__main__":
    main()
