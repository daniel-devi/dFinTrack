from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Third-party Libraries
from PIL import Image
from cryptography.fernet import Fernet
import base64
import os


#* Create your models here.

#* User Profile 
class UserProfile(models.Model):
    # Functions
    
    def user_profile_image_directory_path(instance, filename): # Profile Save Directory
        # file will be uploaded to MEDIA_ROOT/user_name/<filename>
        return f"Profile-Images/user_{instance.user.username}/{filename}"
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Relation to a user
    profile_picture = models.ImageField(upload_to=user_profile_image_directory_path, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)
        
        if self.profile_picture : # Checks if there is a Profile Picture First
            # resize the image
            img = Image.open(self.profile_picture.path)
            if img.height > 400 or img.width > 300:
                output_size = (400, 300)
                # create a thumbnail
                img.thumbnail(output_size)
                # overwrite the larger image
                img.save(self.profile_picture.path)

                

#* User Card Payment Detail

# Ensure you have a secret key for encryption stored in settings
if not hasattr(settings, 'ENCRYPTION_KEY'):
    settings.ENCRYPTION_KEY = base64.urlsafe_b64encode(os.urandom(32))

# Function to encrypt sensitive data using cryptography
def encrypt_data(data):
    fernet = Fernet(settings.ENCRYPTION_KEY)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Function to Decrypt sensitive data using cryptography
def decrypt_data(encrypted_data):
    fernet = Fernet(settings.ENCRYPTION_KEY)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# User Payment Card
class PaymentCardDetail(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=255)
    encrypted_card_number = models.BinaryField(editable=False) # Hides it from Admin Panel 
    encrypted_expiry_date = models.BinaryField(editable=False) #*
    encrypted_cvv = models.BinaryField(editable=False) #*
    created_at = models.DateTimeField(auto_now_add=True)

    def set_card_number(self, card_number):
        self.encrypted_card_number = encrypt_data(card_number)

    def get_card_number(self):
        return decrypt_data(self.encrypted_card_number)

    def set_expiry_date(self, expiry_date):
        self.encrypted_expiry_date = encrypt_data(expiry_date)

    def get_expiry_date(self):
        return decrypt_data(self.encrypted_expiry_date)

    def set_cvv(self, cvv):
        self.encrypted_cvv = encrypt_data(cvv)

    def get_cvv(self):
        return decrypt_data(self.encrypted_cvv)

    def save(self, *args, **kwargs):
        # Override save to ensure data is always encrypted
        self.encrypted_card_number = encrypt_data(self.get_card_number())
        self.encrypted_expiry_date = encrypt_data(self.get_expiry_date())
        self.encrypted_cvv = encrypt_data(self.get_cvv())
        super().save(*args, **kwargs)
        
     
   
#* A User Account Model
class Account(models.Model):
    # Choice variable
    
    ACCOUNT_TYPES = [
        ('savings', 'Savings'),
        ('current', 'Current'),
        ('checking', 'Checking'),
        ('investment', 'Investment'),
        ('credit', 'Credit'),
        # Add more account types as needed
    ]
    
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
        
        
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user who owns the Account
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPES) # e.g., Savings, Checking
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) # User Account Balance Eg: (currency) 100.00
    currency = models.CharField(max_length=10, null=True, blank=True)  # Account Currency Eg: USD
    created_at = models.DateTimeField(auto_now_add=True) # Date Account was Created
    updated_at = models.DateTimeField(auto_now=True) # Date Account was Updated

    # Return the Name of Each Object as {User-Username} Profile
    def __str__(self):
        return f"{self.user.username} ({self.account_type})- {self.currency} {self.balance}"
 