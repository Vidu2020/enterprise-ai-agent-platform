def assign_team(category):

    mapping = {
        "VPN" : "Network Team",
        "Password":"Access Team",
        "Software":"Desktop Team"
    }

    return mapping.get(category,"Service_Desk")