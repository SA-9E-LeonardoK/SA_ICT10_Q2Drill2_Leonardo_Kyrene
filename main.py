from pyscript import document  # lets us get things from the webpage

# predefined sets of club members per grade level
grade7 = {"Gu Ran", "Caitlyn Kiramman", "John Reaction", "Steve Lacy"}
grade8 = {"Jiang jia", "Rachel Green", "Faye Webster"}
grade9 = {"Park Jihyo", "Chandler Bing", "Frank Ocean", "Paige Turner"}
grade10 = {"Beatrice Laus", "Kim Dahyun", "Rei Ayanami"}

# empty set that will store the members added by the user
new_members = set()


def add_member(e):  # e is for the event handler
    # get the first and last name from the text boxes
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value

    # combine the names into one and remove extra spaces
    full_name = f"{first} {last}".strip().title()

    # add the new member to the set of new members
    new_members.add(full_name)

    # combine all the sets using the union operator (|)
    all_members = grade7 | grade8 | grade9 | grade10 | new_members

    # remove empty names using the difference operator (-)
    all_members = all_members - {""}

    # sort the members so they show in order, then put each on a new line
    member_list = "<br>".join(sorted(all_members))

    # total number of members
    total = len(all_members)

    # show the results on the webpage using an f-string
    document.getElementById("output1").innerHTML = (
        f"<b>All members:</b><br>{member_list}<br><br>"
        f"<b>Total members: {total}</b>"
    )
