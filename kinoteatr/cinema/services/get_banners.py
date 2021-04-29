def get_singleton_inst(model):
    inst = model.load()
    if not inst.status:  # if page has inactive status - we don`t have to send it to template
        return None
    return inst
