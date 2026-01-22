class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, item, quantity=1):
        item_id = str(item.id)

        if item_id not in self.cart:
            self.cart[item_id] = {
                "title": item.title,
                "price": float(item.price),
                "quantity": quantity
            }
        else:
            self.cart[item_id]["quantity"] += quantity

        self.session.modified = True

    @property
    def count(self):
        return sum(item["quantity"] for item in self.cart.values())