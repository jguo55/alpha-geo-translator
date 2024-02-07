# alpha-geo-translator
Script that takes alpha geometry formatted data and does conversions based off of provided translation table.
Still working on translating ? statements because those translations aren't provided.
TO USE:
Drag input txt file into same folder as the script. Change file name to "input.txt" (or you can change which file the program reads)
Outputs to the same folder in translated.txt

Expected formatting: First line problem name, Second Line format
Example Input:
translated_imo_2000_p1
a b = segment a b; g1 = on_tline g1 a a b; g2 = on_tline g2 b b a; m = on_circle m g1 a, on_circle m g2 b; n = on_circle n g1 a, on_circle n g2 b; c = on_pline c m a b, on_circle c g1 a; d = on_pline d m a b, on_circle d g2 b; e = on_line e a c, on_line e b d; p = on_line p a n, on_line p c d; q = on_line q b n, on_line q c d ? cong e p e q

Example Output:
translated_imo_2000_p1
Construct 2 distinct points A, B. Construct G1 such that G1A is perpendicular to AB. Construct G2 such that G2B is perpendicular to BA. Construct M on circle such that G1A = G1M. Construct M on circle such that G2B = G2M. Construct N on circle such that G1A = G1N. Construct N on circle such that G2B = G2N. Construct C such that CM is parallel to AB. Construct C on circle such that G1A = G1C. Construct D such that DM is parallel to AB. Construct D on circle such that G2B = G2D. Construct E such that line AC. Construct E such that line BD. Construct P such that line AN. Construct P such that line CD. Construct Q such that line BN. Construct Q such that line CD. Show that EP = EQ. 

![image](https://github.com/jguo55/alpha-geo-translator/assets/148511131/3df9a420-07c9-4c98-ac9d-fab6121c7b3b)
