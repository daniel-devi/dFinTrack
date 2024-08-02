from django.db import models
from django.contrib.auth.models import User
# Third-Party Libraries
from uuid import uuid4
# Accounts
from Accounts.models import Account

#* Create your models here.


#* Model For ExpenseCategory
class ExpenseCategory(models.Model):
    # Choice Variable
    
    CATEGORY_TYPES = (
        ('Food', 'Food & Dining'),
        ('Utilities', 'Utilities'),
        ('Entertainment', 'Entertainment'),
        ('Health', 'Health & Fitness'),
        ('Travel', 'Travel'),
        ('Education', 'Education'),
        ('Shopping', 'Shopping'),
        ('Transportation', 'Transportation'),
        ('Housing', 'Housing'),
        ('Other', 'Other'),
    )


    name = models.CharField(max_length=100, unique=True)  # Name of the category
    description = models.TextField(blank=True, null=True)  # Description of the category
    category_type = models.CharField(max_length=50, choices=CATEGORY_TYPES)  # Type of category
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # User who created the category
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the category was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the category was last updated

    
    def __str__(self):
        return f"{self.name}- {self.category_type} at {self.created_at} by {self.created_by}"


#* Model For Transactions
class Transaction(models.Model):
    # Choices Variable
     
    TRANSACTION_TYPES = (
        ('debit', 'Debit'),
        ('credit', 'Credit'),
        ('purchase', 'Purchase'),
        ('refund', 'Refund'),
        # TODO: Add more transaction types as needed
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        # TODO: Add more statuses as needed
    )
    
    CURRENCY_CHOICES = [
    ('AED', 'United Arab Emirates Dirham'),
    ('AFN', 'Afghan Afghani'),
    ('ALL', 'Albanian Lek'),
    ('AMD', 'Armenian Dram'),
    ('ANG', 'Netherlands Antillean Guilder'),
    ('AOA', 'Angolan Kwanza'),
    ('ARS', 'Argentine Peso'),
    ('AUD', 'Australian Dollar'),
    ('AWG', 'Aruban Florin'),
    ('AZN', 'Azerbaijani Manat'),
    ('BAM', 'Bosnia-Herzegovina Convertible Mark'),
    ('BBD', 'Barbadian Dollar'),
    ('BDT', 'Bangladeshi Taka'),
    ('BGN', 'Bulgarian Lev'),
    ('BHD', 'Bahraini Dinar'),
    ('BIF', 'Burundian Franc'),
    ('BMD', 'Bermudian Dollar'),
    ('BND', 'Brunei Dollar'),
    ('BOB', 'Bolivian Boliviano'),
    ('BRL', 'Brazilian Real'),
    ('BSD', 'Bahamian Dollar'),
    ('BTN', 'Bhutanese Ngultrum'),
    ('BWP', 'Botswana Pula'),
    ('BYN', 'Belarusian Ruble'),
    ('BZD', 'Belize Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('CDF', 'Congolese Franc'),
    ('CHF', 'Swiss Franc'),
    ('CLP', 'Chilean Peso'),
    ('CNY', 'Chinese Yuan'),
    ('COP', 'Colombian Peso'),
    ('CRC', 'Costa Rican Colón'),
    ('CUP', 'Cuban Peso'),
    ('CVE', 'Cape Verdean Escudo'),
    ('CZK', 'Czech Koruna'),
    ('DJF', 'Djiboutian Franc'),
    ('DKK', 'Danish Krone'),
    ('DOP', 'Dominican Peso'),
    ('DZD', 'Algerian Dinar'),
    ('EGP', 'Egyptian Pound'),
    ('ERN', 'Eritrean Nakfa'),
    ('ETB', 'Ethiopian Birr'),
    ('EUR', 'Euro'),
    ('FJD', 'Fijian Dollar'),
    ('FKP', 'Falkland Islands Pound'),
    ('FOK', 'Faroese Króna'),
    ('GBP', 'British Pound'),
    ('GEL', 'Georgian Lari'),
    ('GGP', 'Guernsey Pound'),
    ('GHS', 'Ghanaian Cedi'),
    ('GIP', 'Gibraltar Pound'),
    ('GMD', 'Gambian Dalasi'),
    ('GNF', 'Guinean Franc'),
    ('GTQ', 'Guatemalan Quetzal'),
    ('GYD', 'Guyanese Dollar'),
    ('HKD', 'Hong Kong Dollar'),
    ('HNL', 'Honduran Lempira'),
    ('HRK', 'Croatian Kuna'),
    ('HTG', 'Haitian Gourde'),
    ('HUF', 'Hungarian Forint'),
    ('IDR', 'Indonesian Rupiah'),
    ('ILS', 'Israeli New Shekel'),
    ('IMP', 'Isle of Man Pound'),
    ('INR', 'Indian Rupee'),
    ('IQD', 'Iraqi Dinar'),
    ('IRR', 'Iranian Rial'),
    ('ISK', 'Icelandic Króna'),
    ('JEP', 'Jersey Pound'),
    ('JMD', 'Jamaican Dollar'),
    ('JOD', 'Jordanian Dinar'),
    ('JPY', 'Japanese Yen'),
    ('KES', 'Kenyan Shilling'),
    ('KGS', 'Kyrgyzstani Som'),
    ('KHR', 'Cambodian Riel'),
    ('KID', 'Kiribati Dollar'),
    ('KMF', 'Comorian Franc'),
    ('KRW', 'South Korean Won'),
    ('KWD', 'Kuwaiti Dinar'),
    ('KYD', 'Cayman Islands Dollar'),
    ('KZT', 'Kazakhstani Tenge'),
    ('LAK', 'Lao Kip'),
    ('LBP', 'Lebanese Pound'),
    ('LKR', 'Sri Lankan Rupee'),
    ('LRD', 'Liberian Dollar'),
    ('LSL', 'Lesotho Loti'),
    ('LYD', 'Libyan Dinar'),
    ('MAD', 'Moroccan Dirham'),
    ('MDL', 'Moldovan Leu'),
    ('MGA', 'Malagasy Ariary'),
    ('MKD', 'Macedonian Denar'),
    ('MMK', 'Myanmar Kyat'),
    ('MNT', 'Mongolian Tögrög'),
    ('MOP', 'Macanese Pataca'),
    ('MRU', 'Mauritanian Ouguiya'),
    ('MUR', 'Mauritian Rupee'),
    ('MVR', 'Maldivian Rufiyaa'),
    ('MWK', 'Malawian Kwacha'),
    ('MXN', 'Mexican Peso'),
    ('MYR', 'Malaysian Ringgit'),
    ('MZN', 'Mozambican Metical'),
    ('NAD', 'Namibian Dollar'),
    ('NGN', 'Nigerian Naira'),
    ('NIO', 'Nicaraguan Córdoba'),
    ('NOK', 'Norwegian Krone'),
    ('NPR', 'Nepalese Rupee'),
    ('NZD', 'New Zealand Dollar'),
    ('OMR', 'Omani Rial'),
    ('PAB', 'Panamanian Balboa'),
    ('PEN', 'Peruvian Sol'),
    ('PGK', 'Papua New Guinean Kina'),
    ('PHP', 'Philippine Peso'),
    ('PKR', 'Pakistani Rupee'),
    ('PLN', 'Polish Złoty'),
    ('PYG', 'Paraguayan Guaraní'),
    ('QAR', 'Qatari Riyal'),
    ('RON', 'Romanian Leu'),
    ('RSD', 'Serbian Dinar'),
    ('RUB', 'Russian Ruble'),
    ('RWF', 'Rwandan Franc'),
    ('SAR', 'Saudi Riyal'),
    ('SBD', 'Solomon Islands Dollar'),
    ('SCR', 'Seychellois Rupee'),
    ('SDG', 'Sudanese Pound'),
    ('SEK', 'Swedish Krona'),
    ('SGD', 'Singapore Dollar'),
    ('SHP', 'Saint Helena Pound'),
    ('SLL', 'Sierra Leonean Leone'),
    ('SOS', 'Somali Shilling'),
    ('SRD', 'Surinamese Dollar'),
    ('SSP', 'South Sudanese Pound'),
    ('STN', 'São Tomé and Príncipe Dobra'),
    ('SYP', 'Syrian Pound'),
    ('SZL', 'Eswatini Lilangeni'),
    ('THB', 'Thai Baht'),
    ('TJS', 'Tajikistani Somoni'),
    ('TMT', 'Turkmenistani Manat'),
    ('TND', 'Tunisian Dinar'),
    ('TOP', 'Tongan Paʻanga'),
    ('TRY', 'Turkish Lira'),
    ('TTD', 'Trinidad and Tobago Dollar'),
    ('TVD', 'Tuvaluan Dollar'),
    ('TWD', 'New Taiwan Dollar'),
    ('TZS', 'Tanzanian Shilling'),
    ('UAH', 'Ukrainian Hryvnia'),
    ('UGX', 'Ugandan Shilling'),
    ('USD', 'United States Dollar'),
    ('UYU', 'Uruguayan Peso'),
    ('UZS', 'Uzbekistani Soʻm'),
    ('VED', 'Venezuelan Bolívar'),
    ('VND', 'Vietnamese Đồng'),
    ('VUV', 'Vanuatu Vatu'),
    ('WST', 'Samoan Tālā'),
    ('XAF', 'Central African CFA Franc'),
    ('XCD', 'East Caribbean Dollar'),
    ('XOF', 'West African CFA Franc'),
    ('XPF', 'CFP Franc'),
    ('YER', 'Yemeni Rial'),
    ('ZAR', 'South African Rand'),
    ('ZMW', 'Zambian Kwacha'),
    ('ZWL', 'Zimbabwean Dollar'),
    # TODO: Add more as need
]

    
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User that makes the Transaction object
    account = models.ForeignKey(Account, on_delete=models.CASCADE) # Transaction Model - User Account
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES) # Transaction Type eg: Purchase  
    status = models.CharField(max_length=50, choices=STATUS_CHOICES) # Transaction Status eg: Successful
    currency = models.CharField(max_length=30, choices=CURRENCY_CHOICES) # Transaction Currency eg: $ USD-Dollar
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) # Amount of Transaction
    transaction_uid =  models.UUIDField(default=uuid4, unique=True, editable=True) # Special UID to identify each transaction
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True, blank=True) # Category of Transaction Made
    description = models.CharField(max_length=255, blank=True, null=True) # Optional Transaction Details
    timestamp = models.DateTimeField(auto_now_add=True, editable=True) # Time of the Transaction
    
    def __str__(self):
        return f"{self.CURRENCY_CHOICES} {self.amount} on {self.date} - {self.description}"


#* Model Budgets
class Budget(models.Model):
    name = models.CharField(max_length=100)  # Name of the budget
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who owns the budget
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)  # Expense category for the budget
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Budgeted amount
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)# Budgeted amount_spent
    valid = models.BooleanField(default=True)
    start_date = models.DateField()  # Start date of the budget period
    end_date = models.DateField()  # End date of the budget period
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the budget was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the budget was last updated

    def __str__(self):
        return f'{self.name} - {self.category.name}'

    class Meta:
        unique_together = ('user', 'category', 'start_date', 'end_date')  # Ensure no duplicate budgets for the same category and period

# Model for Financial Goal
class FinancialGoal(models.Model):
    # Choice Variable
    
    GOAL_TYPES = (
        ('savings', 'Savings'),
        ('investment', 'Investment'),
        ('debt_repayment', 'Debt Repayment'),
        ('emergency_fund', 'Emergency Fund'),
        ('retirement', 'Retirement'),
        ('purchase', 'Purchase'),
        ('other', 'Other'),
    )


    name = models.CharField(max_length=100)  # Name of the goal
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who owns the goal
    goal_type = models.CharField(max_length=50, choices=GOAL_TYPES)  # Type of financial goal
    target_amount = models.DecimalField(max_digits=15, decimal_places=2)  # Target amount to achieve
    current_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # Current amount saved/invested towards the goal
    start_date = models.DateField()  # Start date of the goal
    target_date = models.DateField()  # Target date to achieve the goal
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the goal was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the goal was last updated
    description = models.TextField(blank=True, null=True)  # Optional description of the goal

    def __str__(self):
        return f'{self.name} - {self.goal_type}'

    class Meta:
        unique_together = ('user', 'name', 'goal_type')  # Ensure no duplicate goals with the same name and type for a user

#* A Notification 
class Notification(models.Model):
    # Choices Variable
    
    NOTIFICATION_TYPES = (
        ('transaction_success', 'Transaction Success'),
        ('budget_limit', 'Budget Limit Reached'),
        ('budget_deadline', 'Budget End Date Reached'),
        ('payment_due', 'Payment Due'),
        ('general', 'General Notification'),
        #TODO: Add more as needed
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who receives the notification
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)  # Type of notification
    message = models.TextField()  # Content of the notification
    is_read = models.BooleanField(default=False)  # Status to track if the notification has been read
    created_at = models.DateTimeField(auto_now_add=True)  # When the notification was created

    def __str__(self):
        return f"Notification for {self.user.username} - {self.notification_type}"

#* A Update Model for Alert

class Update(models.Model):
    # Choice Variable
    
    UPDATE_TYPES = (
        ('budget_update', 'Budget Update'),
        ('account_update', 'Account Update'),
        ('transaction_update', 'Transaction Update'),
        #TODO: Add more as needed
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user affected by the update
    update_type = models.CharField(max_length=50, choices=UPDATE_TYPES)  # Type of update
    message = models.TextField()  # Content of the update
    created_at = models.DateTimeField(auto_now_add=True)  # When the update was created

    def __str__(self):
        return f"Update for {self.user.username} - {self.update_type}"
