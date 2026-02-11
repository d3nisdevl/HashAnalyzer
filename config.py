HASH_TYPES = {
    'MD5': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}$',
        'desc': 'MD5 Hash',
        'hashcat': '-m 0'
    },
    
    'SHA1': {
        'length': 40,
        'pattern': r'^[a-f0-9]{40}$',
        'desc': 'SHA-1 Hash',
        'hashcat': '-m 100'
    },
    
    'SHA256': {
        'length': 64,
        'pattern': r'^[a-f0-9]{64}$',
        'desc': 'SHA-256 Hash',
        'hashcat': '-m 1400'
    },
    
    'SHA512': {
        'length': 128,
        'pattern': r'^[a-f0-9]{128}$',
        'desc': 'SHA-512 Hash',
        'hashcat': '-m 1700'
    },
    
    'SHA224': {
        'length': 56,
        'pattern': r'^[a-f0-9]{56}$',
        'desc': 'SHA-224 Hash',
        'hashcat': '-m 1300'
    },
    
    'SHA384': {
        'length': 96,
        'pattern': r'^[a-f0-9]{96}$',
        'desc': 'SHA-384 Hash',
        'hashcat': '-m 10800'
    },
    
    'MySQL': {
        'length': 16,
        'pattern': r'^[a-f0-9]{16}$',
        'desc': 'MySQL Hash',
        'hashcat': '-m 300'
    },

    'MySQL5': {
        'length': 40,
        'pattern': r'^\*[A-F0-9]{40}$',
        'desc': 'MySQL 5.x Hash',
        'hashcat': '-m 300'
    },
    
    'NTLM': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}$',
        'desc': 'NTLM Hash',
        'hashcat': '-m 1000'
    },
    
    'BCRYPT': {
        'length': 60,
        'pattern': r'^\$2[aby]\$\d+\$[./A-Za-z0-9]{53}$',
        'desc': 'bcrypt Hash',
        'hashcat': '-m 3200'
    },
    
    'MD4': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}$',
        'desc': 'MD4 Hash',
        'hashcat': '-m 900'
    },
    
    'MD5Crypt': {
        'length': 34,
        'pattern': r'^\$1\$[./A-Za-z0-9]{8}\$[./A-Za-z0-9]{22}$',
        'desc': 'MD5 Crypt',
        'hashcat': '-m 500'
    },
    
    'SHA256Crypt': {
        'length': 55,
        'pattern': r'^\$5\$[./A-Za-z0-9]{16}\$[./A-Za-z0-9]{43}$',
        'desc': 'SHA-256 Crypt',
        'hashcat': '-m 7400'
    },
    
    'SHA512Crypt': {
        'length': 106,
        'pattern': r'^\$6\$[./A-Za-z0-9]{16}\$[./A-Za-z0-9]{86}$',
        'desc': 'SHA-512 Crypt',
        'hashcat': '-m 1800'
    },
    
    'MD5 Salt': {
        'length': 48,
        'pattern': r'^[a-f0-9]{32}:[a-f0-9]{16}$',
        'desc': 'MD5 with Salt',
        'hashcat': '-m 10'
    },
    
    'SHA1 Salt': {
        'length': 56,
        'pattern': r'^[a-f0-9]{40}:[a-f0-9]{16}$',
        'desc': 'SHA-1 with Salt',
        'hashcat': '-m 110'
    },
    
    'SHA256 Salt': {
        'length': 80,
        'pattern': r'^[a-f0-9]{64}:[a-f0-9]{16}$',
        'desc': 'SHA-256 with Salt',
        'hashcat': '-m 1410'
    },
    
    'Apache MD5': {
        'length': 36,
        'pattern': r'^\$apr1\$[./A-Za-z0-9]{8}\$[./A-Za-z0-9]{22}$',
        'desc': 'Apache MD5',
        'hashcat': '-m 1600'
    },
    
    'PostgreSQL': {
        'length': 32,
        'pattern': r'^md5[a-f0-9]{32}$',
        'desc': 'PostgreSQL MD5',
        'hashcat': '-m 12'
    },
    
    'MSSQL': {
        'length': 54,
        'pattern': r'^0x0100[a-f0-9]{48}$',
        'desc': 'MSSQL Hash',
        'hashcat': '-m 131'
    },
    
    'Oracle': {
        'length': 16,
        'pattern': r'^[A-F0-9]{16}$',
        'desc': 'Oracle 7-10g',
        'hashcat': '-m 3100'
    },
    
    'LM Hash': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}$',
        'desc': 'LAN Manager Hash',
        'hashcat': '-m 3000'
    },
    
    'Wordpress': {
        'length': 34,
        'pattern': r'^\$P\$[./A-Za-z0-9]{31}$',
        'desc': 'Wordpress MD5',
        'hashcat': '-m 400'
    },
    
    'Joomla': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}:[a-f0-9]{32}$',
        'desc': 'Joomla Hash',
        'hashcat': '-m 11'
    },
    
    'SHA3-256': {
        'length': 64,
        'pattern': r'^[a-f0-9]{64}$',
        'desc': 'SHA3-256 Hash',
        'hashcat': '-m 17400'
    },
    
    'SHA3-512': {
        'length': 128,
        'pattern': r'^[a-f0-9]{128}$',
        'desc': 'SHA3-512 Hash',
        'hashcat': '-m 17600'
    },
    
    'CRC32': {
        'length': 8,
        'pattern': r'^[a-f0-9]{8}$',
        'desc': 'CRC32 Hash',
        'hashcat': '-m 11500'
    },

    'PHPS': {
        'length': 34,
        'pattern': r'^\$P\$[./A-Za-z0-9]{31}$',
        'desc': 'PHPS Password Hash',
        'hashcat': '-m 400'
    },

    # Дополнительные популярные хеши
    'Blowfish': {
        'length': 60,
        'pattern': r'^\$2[axy]\$\d+\$[./A-Za-z0-9]{53}$',
        'desc': 'Blowfish Hash',
        'hashcat': '-m 3200'
    },
    
    'Django MD5': {
        'length': 32,
        'pattern': r'^md5\$[a-f0-9]+\$[a-f0-9]{32}$',
        'desc': 'Django MD5',
        'hashcat': '-m 10'
    },
    
    'Django SHA1': {
        'length': 40,
        'pattern': r'^sha1\$[a-f0-9]+\$[a-f0-9]{40}$',
        'desc': 'Django SHA1',
        'hashcat': '-m 120'
    },
    
    'Django BCrypt': {
        'length': 60,
        'pattern': r'^bcrypt\$[a-f0-9]+\$[a-f0-9]{53}$',
        'desc': 'Django BCrypt',
        'hashcat': '-m 3200'
    },
    
    'Django PBKDF2': {
        'length': 64,
        'pattern': r'^pbkdf2_sha256\$\d+\$[A-Za-z0-9+/]+\$[A-Za-z0-9+/=]+$',
        'desc': 'Django PBKDF2 SHA256',
        'hashcat': '-m 10000'
    },
    
    'LDAP MD5': {
        'length': 32,
        'pattern': r'^\{MD5\}[A-Za-z0-9+/=]{22,24}$',
        'desc': 'LDAP MD5',
        'hashcat': '-m 0'
    },
    
    'LDAP SHA1': {
        'length': 28,
        'pattern': r'^\{SHA\}[A-Za-z0-9+/=]{27,28}$',
        'desc': 'LDAP SHA1',
        'hashcat': '-m 100'
    },
    
    'LDAP SSHA': {
        'length': 32,
        'pattern': r'^\{SSHA\}[A-Za-z0-9+/=]{32,}$',
        'desc': 'LDAP Salted SHA1',
        'hashcat': '-m 111'
    },
    
    'LDAP CRYPT': {
        'length': 13,
        'pattern': r'^\{CRYPT\}.+$',
        'desc': 'LDAP Crypt',
        'hashcat': '-m 1800'
    },
    
    'Cisco Type 7': {
        'length': 4,
        'pattern': r'^[0-9A-Fa-f]{4,}$',
        'desc': 'Cisco Type 7 Password',
        'hashcat': '-m 1500'
    },
    
    'Cisco Type 5': {
        'length': 32,
        'pattern': r'^\$1\$[a-f0-9]{8}\$[a-f0-9]{22}$',
        'desc': 'Cisco Type 5 (MD5)',
        'hashcat': '-m 500'
    },
    
    'Cisco Type 9': {
        'length': 60,
        'pattern': r'^\$8\$[./A-Za-z0-9]{53}$',
        'desc': 'Cisco Type 9 (scrypt)',
        'hashcat': '-m 7400'
    },
    
    'JWT': {
        'length': 0,
        'pattern': r'^eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*$',
        'desc': 'JSON Web Token',
        'hashcat': '-m 16500'
    },
    
    'RIPEMD-160': {
        'length': 40,
        'pattern': r'^[a-f0-9]{40}$',
        'desc': 'RIPEMD-160 Hash',
        'hashcat': '-m 6000'
    },
    
    'Whirlpool': {
        'length': 128,
        'pattern': r'^[a-f0-9]{128}$',
        'desc': 'Whirlpool Hash',
        'hashcat': '-m 6100'
    },
    
    'Keccak-256': {
        'length': 64,
        'pattern': r'^[a-f0-9]{64}$',
        'desc': 'Keccak-256 Hash',
        'hashcat': '-m 17800'
    },
    
    'Keccak-512': {
        'length': 128,
        'pattern': r'^[a-f0-9]{128}$',
        'desc': 'Keccak-512 Hash',
        'hashcat': '-m 17900'
    },
    
    'Argon2': {
        'length': 0,
        'pattern': r'^\$argon2[id]?\$v=\d+\$m=\d+,t=\d+,p=\d+\$[A-Za-z0-9+/]+\$[A-Za-z0-9+/]+$',
        'desc': 'Argon2 Hash',
        'hashcat': '-m 20800'
    },
    
    'SCRYPT': {
        'length': 0,
        'pattern': r'^\$7\$[./A-Za-z0-9]{86}$',
        'desc': 'SCRYPT Hash',
        'hashcat': '-m 8900'
    },
    
    'MongoDB SCRAM': {
        'length': 0,
        'pattern': r'^SCRAM-SHA-1\$[0-9]+\$[A-Za-z0-9+/=]+\$[A-Za-z0-9+/=]+\$[A-Za-z0-9+/=]+$',
        'desc': 'MongoDB SCRAM Hash',
        'hashcat': '-m 18200'
    },
    
    'VBulletin': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}:[a-f0-9]{3,32}$',
        'desc': 'vBulletin Hash',
        'hashcat': '-m 2611'
    },
    
    'IPB': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}:[a-f0-9]{8}$',
        'desc': 'Invision Power Board',
        'hashcat': '-m 2811'
    },
    
    'MyBB': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}:[a-f0-9]{8}$',
        'desc': 'MyBB Hash',
        'hashcat': '-m 2811'
    },
    
    'PHPPass': {
        'length': 34,
        'pattern': r'^\$H\$[./A-Za-z0-9]{31}$',
        'desc': 'PHPPass Hash',
        'hashcat': '-m 400'
    },
    
    'Radmin2': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}$',
        'desc': 'Radmin2 Hash',
        'hashcat': '-m 9900'
    },
    
    'SIP': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}$',
        'desc': 'SIP MD5 Hash',
        'hashcat': '-m 11400'
    },
    
    'HMAC-SHA1': {
        'length': 40,
        'pattern': r'^[a-f0-9]{40}$',
        'desc': 'HMAC-SHA1',
        'hashcat': '-m 160'
    },
    
    'Kerberos 5 TGS-REP': {
        'length': 0,
        'pattern': r'^\$krb5tgs\$23\$.+$',
        'desc': 'Kerberos 5 TGS-REP',
        'hashcat': '-m 13100'
    },
    
    'DPAPI': {
        'length': 0,
        'pattern': r'^[a-f0-9]{64}:[a-f0-9]{512,}$',
        'desc': 'DPAPI Master Key',
        'hashcat': '-m 15300'
    },
    
    'Bitcoin Wallet': {
        'length': 64,
        'pattern': r'^[a-f0-9]{64}$',
        'desc': 'Bitcoin Wallet Hash',
        'hashcat': '-m 11300'
    },
    
    'Ethereum Wallet': {
        'length': 64,
        'pattern': r'^[a-f0-9]{64}$',
        'desc': 'Ethereum Wallet Hash',
        'hashcat': '-m 15700'
    },
    
    'LastPass': {
        'length': 32,
        'pattern': r'^[a-f0-9]{32}$',
        'desc': 'LastPass Hash',
        'hashcat': '-m 6800'
    },
    
    '1Password': {
        'length': 43,
        'pattern': r'^[A-Za-z0-9+/]{43}$',
        'desc': '1Password Hash',
        'hashcat': '-m 6600'
    },
    
    'KeePass': {
        'length': 64,
        'pattern': r'^[a-f0-9]{64}$',
        'desc': 'KeePass Hash',
        'hashcat': '-m 13400'
    }
}