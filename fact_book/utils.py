from measurement import measures


def get_units():
    measurements = {
        # 'Area': measures.Area,
        'Capacitance': measures.Capacitance,
        'Current': measures.Current,
        'Distance': measures.Distance,
        'Energy': measures.Energy,
        'Frequency': measures.Frequency,
        'Mass': measures.Mass,
        'Resistance': measures.Resistance,
        # 'Speed': measures.Speed,
        'Temperature': measures.Temperature,
        'Time': measures.Time,
        'Voltage': measures.Voltage,
        'Volume': measures.Volume,
        # 'Weight': measures.Weight,
    }

    opts = opts_all = []
    for k, v in measurements.items():
        for a, w in v.get_si_aliases().items():
            opts.append((w, '%s (%s)' % (a, (k.lower()))))
            break

    opts_all = [('SI Units', tuple(opts)),]

    for k, v in measurements.items():
        opts = []
        for a, w in v.get_aliases().items():
            if not w == v.STANDARD_UNIT and False:
                opts.append((w, '%s (%s %s)' % (a, v.UNITS.get(w, ''), v.STANDARD_UNIT)))
            else:
                opts.append((w, a))

        opts_all.append((k, tuple(opts)))

    return opts_all
