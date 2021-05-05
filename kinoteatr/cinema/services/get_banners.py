def get_singleton_inst(model):
    inst = model.load()
    if not inst.status:  # if page has inactive status - we don`t have to send it to template
        return None
    return inst


def get_page(pages):
    context = {}
    for page in pages:
        context[page.__name__] = get_singleton_inst(page)
    return context


def get_context_for_generic_views(pages):
    context = {}
    banners_context = get_page(pages)
    context['BackgroundImage'] = banners_context.get('BackgroundImage')
    context['OnTopBanner'] = banners_context.get('OnTopBanner')
    context['MainPage'] = banners_context.get('MainPage')
    context['Advertisement'] = banners_context.get('Advertisement')
    context['AboutCinema'] = banners_context.get('AboutCinema')
    context['CafeBar'] = banners_context.get('CafeBar')

    return context
