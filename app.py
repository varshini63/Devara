from flask import Flask, render_template_string, request, session, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# HTML Templates
BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Convergence - Bahubali X Devara</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
            color: #e0e0e0;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: rgba(30, 35, 60, 0.9);
            border: 2px solid #4a5f8f;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 0 30px rgba(74, 95, 143, 0.3);
        }
        h1 {
            color: #6fa3ef;
            text-align: center;
            margin-bottom: 20px;
            font-size: 2.5em;
            text-shadow: 0 0 10px rgba(111, 163, 239, 0.5);
        }
        h2 {
            color: #8fb4f0;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        .challenge-box {
            background: rgba(20, 25, 45, 0.7);
            border: 1px solid #3a4f7f;
            border-radius: 5px;
            padding: 20px;
            margin: 20px 0;
        }
        .cipher-text {
            background: #0f1420;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            color: #4ade80;
            word-wrap: break-word;
            margin: 15px 0;
            border-left: 4px solid #4ade80;
        }
        .hint {
            color: #fbbf24;
            font-style: italic;
            margin: 15px 0;
            padding: 10px;
            background: rgba(251, 191, 36, 0.1);
            border-left: 3px solid #fbbf24;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            background: #0f1420;
            border: 1px solid #4a5f8f;
            border-radius: 5px;
            color: #e0e0e0;
            font-family: 'Courier New', monospace;
        }
        button {
            background: #4a5f8f;
            color: #fff;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: 1em;
            transition: all 0.3s;
        }
        button:hover {
            background: #6fa3ef;
            box-shadow: 0 0 15px rgba(111, 163, 239, 0.5);
        }
        .error {
            color: #ef4444;
            margin: 10px 0;
            padding: 10px;
            background: rgba(239, 68, 68, 0.1);
            border-left: 3px solid #ef4444;
        }
        .success {
            color: #4ade80;
            margin: 10px 0;
            padding: 10px;
            background: rgba(74, 222, 128, 0.1);
            border-left: 3px solid #4ade80;
        }
        .story {
            color: #9ca3af;
            line-height: 1.8;
            margin: 20px 0;
        }
        code {
            background: #0f1420;
            padding: 2px 6px;
            border-radius: 3px;
            color: #4ade80;
        }
        .legend {
            background: rgba(111, 163, 239, 0.05);
            border-left: 4px solid #6fa3ef;
            padding: 15px;
            margin: 20px 0;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
"""

HOME_TEMPLATE = BASE_TEMPLATE.replace("{% block content %}{% endblock %}", """
    <h1>⚔️ The Convergence: Bahubali X Devara 🌊</h1>
    
    <div class="legend">
        <p style="color: #6fa3ef; font-size: 1.1em; margin-bottom: 10px;">
            <strong>Legend speaks of two great warriors, separated by time yet bound by destiny...</strong>
        </p>
        <p>In the mighty kingdom of Mahishmathi, Bahubali ruled with wisdom and strength. 
        Across the ages, in the depths of the Red Sea, Devara stood as the fearless guardian of the four clans. 
        Though centuries apart, their legacies intertwined through a sacred cipher—a bridge between kingdoms.</p>
        <p style="margin-top: 10px;">Before his final voyage, Devara discovered ancient scrolls from Mahishmathi. 
        He encoded his ultimate secret using techniques that only one who understands both kingdoms could decipher.</p>
    </div>
    
    <div class="story">
        <p><strong>Your Quest:</strong> You are the chosen one—a cryptographer who must prove worthy of both legacies. 
        Navigate through Devara's trials, each guarded by the spirit of the Red Sea. Only then will the gateway 
        to Mahishmathi's final secret reveal itself. Fail, and the convergence remains forever sealed.</p>
    </div>
    
    <div class="challenge-box">
        <h2>🏴‍☠️ The First Trial - The Guardian's Grid</h2>
        <p class="hint">In squares of five by five, where letters dance and hide, the MATRIX reveals all truths. 
        What fairness conceals, the grid shall unveil.</p>
        
        <div class="cipher-text">
            GFBOCPXITRIMDMBZBISZIGSZXDIDIP
        </div>
        
        
        <form method="POST" action="/the-calm-before-storm">
            <input type="text" name="answer" placeholder="Enter the decoded message..." required>
            <button type="submit">Break The First Seal</button>
        </form>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
""")

LAYER2_TEMPLATE = BASE_TEMPLATE.replace("{% block content %}{% endblock %}", """
    <h1>⚡ The Second Trial - Storm of Exclusion ⚡</h1>
    
    <div class="story">
        <p>The first seal breaks, and the sea churns violently. Devara's voice echoes from the depths:</p>
        <p style="color: #8fb4f0; font-style: italic; margin: 15px 0;">
            "In the realm where truth and falsehood dance—where 0 and 1 mate to birth their opposite—
            lies a gate no single key can open. You must try them all, warrior. Every possibility between 
            the void and the complete byte."
        </p>
    </div>
    
    <div class="challenge-box">
        <h2>🔐 The Persistence Challenge</h2>
        <p class="hint">The sea whispers of a technique known only to those who persist. No key was given, no cipher was named. 
        Only through relentless trial will the truth emerge from chaos.</p>
        
        <div class="cipher-text">
            q{vpln'bH_varHuebcrqxetrHOXEj
        </div>

        
        <form method="POST" action="/blood-soaked-waters">
            <input type="text" name="answer" placeholder="flag{...}" required>
            <button type="submit">Conquer The Storm</button>
        </form>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
""")

LAYER3_TEMPLATE = BASE_TEMPLATE.replace("{% block content %}{% endblock %}", """
    <h1>🔱 The Third Trial - The Emperor's Shift 🔱</h1>
    
    <div class="story">
        <p>As the storm subsides, ancient Roman inscriptions appear on the sea walls. Devara's memory speaks:</p>
        <p style="color: #8fb4f0; font-style: italic; margin: 15px 0;">
            "An emperor once secured his messages by shifting the very fabric of language. Not forward, not backward, 
            but to the midpoint of the alphabet's journey. Thirteen steps—the perfect balance where decryption 
            becomes encryption, and encryption becomes decryption."
        </p>
    </div>
    
    <div class="challenge-box">
        <h2>📜 The Symmetrical Transformation</h2>
        <p class="hint">The sea remembers those who never surrender. Try every possibility, from the first to the last."</p>
        
        <div class="cipher-text">
            synt{guvegrra_fuvsgrq_guebhtu_gvzr}
        </div>
        
        
        <form method="POST" action="/the-forgotten-shore">
            <input type="text" name="answer" placeholder="flag{...}" required>
            <button type="submit">Cross The Symmetry</button>
        </form>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
""")

LAYER4_TEMPLATE = BASE_TEMPLATE.replace("{% block content %}{% endblock %}", """
    <h1>🏛️ The Gateway - Mahishmathi's Call 🏛️</h1>
    
    <div class="story">
        <p>You've conquered Devara's trials. The Red Sea parts, revealing a golden gateway inscribed with ancient Telugu script. 
        Behind it lies the final secret—but first, you must prove your knowledge of Mahishmathi itself.</p>
        
        <p style="color: #6fa3ef; margin: 15px 0; padding: 15px; background: rgba(111, 163, 239, 0.1); border-radius: 5px;">
            <strong>Bahubali's Challenge:</strong> "Before you claim the ultimate treasure, speak the name of my kingdom. 
            Not as it appears in chaos, but as it truly is—the throne, the empire, the realm where dharma ruled supreme."
        </p>
    </div>
    
    <div class="challenge-box">
        <h2>👑 The Kingdom's True Name</h2>
        <p class="hint">The inscription reads: "When letters march in columns, ordered by a key only the worthy possess, 
        they whisper secrets. But what key? Think of she who gave Bahubali his greatest strength—his mother, 
        his queen, the warrior goddess herself. Eight letters that commanded respect across all of Mahishmathi. 
        Her name is not just a word—it's a sequence, an order, a pattern that rearranges chaos into truth."</p>
        
        <div class="cipher-text">
            ISMAAMTJAHYHMMRSAHIA
        </div>
        
    
        <form method="POST" action="/mahishmathi-sanctum">
            <input type="text" name="answer" placeholder="The kingdom's name..." required>
            <button type="submit">Unlock Mahishmathi</button>
        </form>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
""")

LAYER5_TEMPLATE = BASE_TEMPLATE.replace("{% block content %}{% endblock %}", """
    <h1>⚔️ The Convergence Chamber ⚔️</h1>
    
    <div class="legend">
        <p style="color: #6fa3ef; font-size: 1.1em;">
            The gateway opens. Before you stands a magnificent chamber where the spirits of Bahubali and Devara converge. 
            Golden pillars from Mahishmathi intertwine with blue coral from the Red Sea. At the center, a final vault 
            bearing both kingdoms' seals.
        </p>
    </div>
    
    <div class="story">
        <p style="color: #8fb4f0; margin: 15px 0;">
            <strong>Bahubali's voice echoes:</strong> "You have proven your worth, warrior. But the greatest treasures 
            require the greatest understanding. My mother's name opened the door, but now you must decode what lies within."
        </p>
        <p style="color: #4ade80; margin: 15px 0;">
            <strong>Devara's voice joins:</strong> "Two kingdoms, one secret. The four clans and Mahishmathi's legacy 
            merge here. Use the queen's wisdom one final time to unlock what centuries have kept hidden."
        </p>
    </div>
    
    <div class="challenge-box">
        <h2>🗝️ The Final Seal - The Ultimate Truth</h2>
        <p class="hint">The vault's inscription glows: "She who gave birth to greatness now gives birth to truth. 
        The same power that revealed the kingdom now reveals the ultimate secret. But this scroll is longer, 
        more complex—eight columns must dance in the queen's order once more. Patience, precision, and the mother's 
        blessing shall reward you with the flag that binds two legends."</p>
        
        <div class="cipher-text">
            wd_3uj4hzmpao0ln3s_ra}4r_4pr4nka_jml54saad_4uhmsre4n_ry_4hw4t
        </div>
        
        <p style="color: #fbbf24; margin-top: 15px;">
            💡 <strong>The Convergence Key:</strong> "The method remains unchanged—columnar transposition with the queen mother's name. 
            But the message is larger, spanning 8 rows beneath her 8-lettered command. Write the cipher in rows of 8, 
            then read the columns in the order her name dictates. Remember: repeated letters in her name create ranked positions."
        </p>
        
        <p style="color: #9ca3af; margin-top: 10px; font-size: 0.9em;">
            <em>Final wisdom: You know her name. You know it unlocks columns. Write 8 characters per row (the ciphertext is 56 chars). 
            Her name's letter ranks tell you: read column X first, column Y second, and so on. The ultimate flag awaits—
            the convergence of Prajala, Mana, Dhana, Samrakshudu, and Mahishmathi's eternal glory.</em>
        </p>
        
        <form method="POST" action="/convergence-complete">
            <input type="text" name="answer" placeholder="w4rz0n3{...}" required>
            <button type="submit">Claim The Convergence</button>
        </form>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
""")

SUCCESS_TEMPLATE = BASE_TEMPLATE.replace("{% block content %}{% endblock %}", """
    <h1>🏆 The Convergence Complete 🏆</h1>
    
    <div class="success">
        <h2>⚔️🌊 Two Legends, One Champion 🌊⚔️</h2>
        <p style="font-size: 1.2em; margin-top: 20px;">
            The spirits of Bahubali and Devara bow before you. You have bridged two kingdoms, conquered four trials, 
            and proven yourself worthy of both legacies. By speaking the true name of Mahishmathi, you have unlocked 
            the ultimate secret.
        </p>
        <div class="cipher-text" style="border-left-color: #4ade80; color: #4ade80; font-size: 1.2em; text-align: center;">
            {{ flag }}
        </div>
    </div>
    
    <div class="legend" style="margin-top: 30px;">
        
        
        <p style="color: #8fb4f0; margin-top: 20px; font-style: italic;">
            <strong>The Secret of DEVASENA:</strong> The queen mother's name unlocked the gateway to Mahishmathi. 
            Her eight letters (D-E-V-A-S-E-N-A) rearranged the cipher text through columnar transposition, revealing 
            the kingdom's true name. With that final key, the convergence was complete.
        </p>
    </div>
    
    <div style="text-align: center; margin-top: 40px; padding: 25px; background: linear-gradient(135deg, rgba(111, 163, 239, 0.1), rgba(74, 222, 128, 0.1)); border-radius: 10px; border: 2px solid rgba(111, 163, 239, 0.3);">
        <p style="color: #6fa3ef; font-size: 1.4em; font-weight: bold; margin-bottom: 15px;">
            "When two legends converge, a new legend is born."
        </p>
        <p style="color: #8fb4f0; font-size: 1.1em; font-style: italic;">
            — From the Red Sea to Mahishmathi, across time and tide
        </p>
        <p style="color: #4ade80; margin-top: 20px; font-size: 1.05em;">
            You are now the keeper of both kingdoms' secrets. 🏛️⚔️🌊
        </p>
    </div>
""")

# Validation functions
def check_layer1(answer):
    expected = "FLAGTHEMATRIXREVEALSALLSECRETS"
    return answer.strip().upper().replace(" ", "") == expected

def check_layer2(answer):
    expected = "flag{y0u_Have_bruteforce_XOR}"
    return answer.strip().lower() == expected.lower()

def check_layer3(answer):
    expected_decoded = "flag{thirteen_shifted_through_time}"
    return answer.strip().lower() == expected_decoded.lower()

def check_layer4(answer):
    expected = "MAHISHMATHISAMRAJYAM"
    return answer.strip().upper().replace(" ", "") == expected

def check_flag(answer):
    expected = "w4rz0n3{pr4j4l4_m4an4_dh4an4_s4mr4k5hudu_y3rr4_s4mudhr4m}"
    return answer.strip() == expected

# Routes
@app.route('/')
def home():
    session.clear()
    return render_template_string(HOME_TEMPLATE, error=None)

@app.route('/the-calm-before-storm', methods=['POST'])
def layer1():
    answer = request.form.get('answer', '')
    if check_layer1(answer):
        session['layer1'] = True
        return redirect(url_for('layer2'))
    return render_template_string(HOME_TEMPLATE, 
        error="Invalid")

@app.route('/blood-soaked-waters')
def layer2():
    if not session.get('layer1'):
        return redirect(url_for('home'))
    return render_template_string(LAYER2_TEMPLATE, error=None)

@app.route('/blood-soaked-waters', methods=['POST'])
def layer2_post():
    if not session.get('layer1'):
        return redirect(url_for('home'))
    answer = request.form.get('answer', '')
    if check_layer2(answer):
        session['layer2'] = True
        return redirect(url_for('layer3'))
    return render_template_string(LAYER2_TEMPLATE, 
        error="The exclusive gates remain sealed. Persistence is key—have you tried EVERY single-byte possibility?")

@app.route('/the-forgotten-shore')
def layer3():
    if not session.get('layer2'):
        return redirect(url_for('home'))
    return render_template_string(LAYER3_TEMPLATE, error=None)

@app.route('/the-forgotten-shore', methods=['POST'])
def layer3_post():
    if not session.get('layer2'):
        return redirect(url_for('home'))
    answer = request.form.get('answer', '')
    if check_layer3(answer):
        session['layer3'] = True
        return redirect(url_for('layer4'))
    return render_template_string(LAYER3_TEMPLATE, 
        error="Invalid")

@app.route('/mahishmathi-sanctum')
def layer4():
    if not session.get('layer3'):
        return redirect(url_for('home'))
    return render_template_string(LAYER4_TEMPLATE, error=None)

@app.route('/mahishmathi-sanctum', methods=['POST'])
def layer4_post():
    if not session.get('layer3'):
        return redirect(url_for('home'))
    answer = request.form.get('answer', '')
    if check_layer4(answer):
        # Directly return the final flag after solving Layer 4
        final_flag = "w4rz0n3{pr4j4l4_m4an4_dh4an4_s4mr4k5hudu_y3rr4_s4mudhr4m}"
        return render_template_string(SUCCESS_TEMPLATE, flag=final_flag)
    return render_template_string(LAYER4_TEMPLATE, 
        error="Invalid")

# Layer 5 routes removed - flag is delivered directly after Layer 4

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)