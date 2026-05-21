import math
import argparse
import sys


class CreditCalculator:
    def run(self):
        parser = argparse.ArgumentParser(
            description="Credit Calculator",
            epilog="Example: python credit_calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10"
        )
        parser.add_argument("--type",      type=str,   help="annuity or diff")
        parser.add_argument("--principal", type=float, help="Loan principal")
        parser.add_argument("--periods",   type=int,   help="Number of months")
        parser.add_argument("--interest",  type=float, help="Annual interest rate")
        parser.add_argument("--payment",   type=float, help="Monthly payment (annuity only)")
        self.args = parser.parse_args()
        self._validate()

        self.i = self.args.interest / (12 * 100)

        if self.args.type == "diff":
            self._calc_diff()
        elif self.args.type == "annuity":
            self._calc_annuity()

    def _validate(self):
        args = self.args

        if args.type not in ("annuity", "diff"):
            self._error()
        if args.type == "diff" and args.payment is not None:
            self._error()
        if args.interest is None:
            self._error()
        for val in [args.principal, args.periods, args.interest, args.payment]:
            if val is not None and val < 0:
                self._error()

    def _error(self):
        print("Incorrect parameters")
        sys.exit()

    def _format_periods(self, n):
        years = n // 12
        months = n % 12
        parts = []
        if years > 0:
            parts.append(f"{years} year{'s' if years > 1 else ''}")
        if months > 0:
            parts.append(f"{months} month{'s' if months > 1 else ''}")
        return " and ".join(parts)

    def _calc_diff(self):
        args = self.args
        if args.principal is None or args.periods is None:
            self._error()
        P, n, i = args.principal, args.periods, self.i
        total_paid = 0
        for m in range(1, n + 1):
            dm = math.ceil(P / n + i * (P - P * (m - 1) / n))
            print(f"Month {m}: payment is {dm}")
            total_paid += dm
        print(f"\nOverpayment = {round(total_paid - P)}")

    def _calc_annuity(self):
        args = self.args
        known = sum([
            args.principal is not None,
            args.periods is not None,
            args.payment is not None,
        ])
        if known < 2:
            self._error()

        i = self.i

        if args.principal is None:
            a, n = args.payment, args.periods
            P = math.floor(a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
            print(f"Your loan principal = {P}!")
            print(f"Overpayment = {round(a * n - P)}")

        elif args.payment is None:
            P, n = args.principal, args.periods
            a = math.ceil(P * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
            print(f"Your annuity payment = {a}!")
            print(f"Overpayment = {round(a * n - P)}")

        elif args.periods is None:
            P, a = args.principal, args.payment
            n = math.ceil(math.log(a / (a - i * P), 1 + i))
            print(f"It will take {self._format_periods(n)} to repay this loan!")
            print(f"Overpayment = {round(a * n - P)}")


if __name__ == "__main__":
    CreditCalculator().run()