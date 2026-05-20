import math
import argparse
import sys


class Stage1:
    def run(self):
        print("Loan principal: 1000")
        print("Month 1: repaid 250")
        print("Month 2: repaid 250")
        print("Month 3: repaid 500")
        print("The loan has been repaid!")


class Stage2:
    def run(self):
        self.principal = float(input("Enter the loan principal:\n> "))

        print('What do you want to calculate?')
        print('type "m" – for number of monthly payments,')
        print('type "p" – for the monthly payment:')
        choice = input("> ").strip().lower()

        if choice == "m":
            self._calc_months()
        elif choice == "p":
            self._calc_payment()

    def _calc_months(self):
        payment = float(input("Enter the monthly payment:\n> "))
        months = math.ceil(self.principal / payment)
        if months == 1:
            print("It will take 1 month to repay the loan")
        else:
            print(f"It will take {months} months to repay the loan")

    def _calc_payment(self):
        months = int(input("Enter the number of months:\n> "))
        payment = math.ceil(self.principal / months)
        last_payment = self.principal - (months - 1) * payment
        if last_payment == payment:
            print(f"Your monthly payment = {payment}")
        else:
            print(f"Your monthly payment = {payment} and the last payment = {int(last_payment)}.")


class Stage3:
    def run(self):
        print("What do you want to calculate?")
        print('type "n" for number of monthly payments,')
        print('type "a" for annuity monthly payment amount,')
        print('type "p" for loan principal:')
        choice = input("> ").strip().lower()

        if choice == "n":
            self._calc_periods()
        elif choice == "a":
            self._calc_payment()
        elif choice == "p":
            self._calc_principal()

    def _calc_periods(self):
        principal = float(input("Enter the loan principal:\n> "))
        payment = float(input("Enter the monthly payment:\n> "))
        interest = float(input("Enter the loan interest:\n> "))
        i = interest / (12 * 100)
        n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
        print(f"It will take {self._format_periods(n)} to repay this loan!")

    def _calc_payment(self):
        principal = float(input("Enter the loan principal:\n> "))
        n = int(input("Enter the number of periods:\n> "))
        interest = float(input("Enter the loan interest:\n> "))
        i = interest / (12 * 100)
        payment = math.ceil(principal * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
        print(f"Your monthly payment = {payment}!")

    def _calc_principal(self):
        payment = float(input("Enter the annuity payment:\n> "))
        n = int(input("Enter the number of periods:\n> "))
        interest = float(input("Enter the loan interest:\n> "))
        i = interest / (12 * 100)
        principal = round(payment / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
        print(f"Your loan principal = {principal}!")

    def _format_periods(self, n):
        years = n // 12
        months = n % 12
        parts = []
        if years > 0:
            parts.append(f"{years} year{'s' if years > 1 else ''}")
        if months > 0:
            parts.append(f"{months} month{'s' if months > 1 else ''}")
        return " and ".join(parts)


class Stage4:
    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--type", type=str)
        parser.add_argument("--principal", type=float)
        parser.add_argument("--periods", type=int)
        parser.add_argument("--interest", type=float)
        parser.add_argument("--payment", type=float)
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
            P = round(a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
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
    if len(sys.argv) > 1:
        Stage4().run()
    else:
        print("Credit Calculator")
        print("Select stage: 1, 2, or 3")
        stage = input("> ").strip()
        stages = {"1": Stage1, "2": Stage2, "3": Stage3}
        if stage in stages:
            stages[stage]().run()
        else:
            print("Invalid stage")