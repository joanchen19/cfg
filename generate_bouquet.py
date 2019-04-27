def bouquet_generator(form_data):
    palette = form_data["palette"]
    flower = form_data["flower_type"].lower()
    greenery = form_data["foliage_type"].lower()

    if palette == "beautiful_blue":
        if flower == "rose":
            bouquet = "blue_rose.jpg"
        if flower == "lily":
            bouquet = "blue_lily.jpg"
        if flower == "orchid":
            bouquet = "blue_orchid.jpg"
        if flower == "daisy":
            bouquet = "blue_daisy.jpg"
        if flower == "tulip":
            bouquet = "blue_tulip.jpg"
        else:
            bouquet = "blue_combo.jpg"
    elif palette == "red":
        if flower == "rose":
            bouquet = "red_rose.jpg"
        if flower == "lily":
            bouquet = "red_lily.jpg"
        if flower == "orchid":
            bouquet = "red_orchid.jpg"
        if flower == "daisy":
            bouquet = "red_daisy.jpg"
        if flower == "tulip":
            bouquet = "red_tulip.jpg"
        else:
            bouquet = "red_combo.jpg"
    elif palette == "pretty_pink":
        if flower == "rose":
            bouquet = "pink_rose.jpg"
        if flower == "lily":
            bouquet = "pink_lily.jpg"
        if flower == "orchid":
            bouquet = "pink_orchid.jpg"
        if flower == "daisy":
            bouquet = "pink_daisy.jpg"
        if flower == "tulip":
            bouquet = "pink_tulip.jpg"
        else:
            bouquet = "pink_combo.jpg"
    elif palette == "colour_pop":
        if flower == "rose":
            bouquet = "bright_rose.jpg"
        if flower == "lily":
            bouquet = "bright_lily.jpg"
        if flower == "orchid":
            bouquet = "bright_orchid.jpg"
        if flower == "daisy":
            bouquet = "bright_daisy.jpg"
        if flower == "tulip":
            bouquet = "bright_tulip.jpg"
        else:
            bouquet = "bright_combo.jpg"
    elif palette == "pastel_perfection":
        if flower == "rose":
            bouquet = "pastel_rose.jpg"
        if flower == "lily":
            bouquet = "pastel_lily.jpg"
        if flower == "orchid":
            bouquet = "pastel_orchid.jpg"
        if flower == "daisy":
            bouquet = "pastel_daisy.jpg"
        if flower == "tulip":
            bouquet = "pastel_tulip.jpg"
        else:
            bouquet = "pastel_combo.jpg"
    return bouquet
