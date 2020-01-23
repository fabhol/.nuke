import nuke
def start(node,samples):
    with node:
        curve = nuke.toNode('TimeDissolve')['lut']
        samples = 100
        previous_value = 0
        distance = 0
        value_dict = {}
        for n in xrange(0,samples):
            x = 1.0/(samples-1)*n
            value = curve.getValueAt(x)
            if n > 0:
                distance += abs(value-previous_value)
            value_dict[x] = distance
            previous_value = value
        tw_lookup = nuke.toNode('TimeWarp')['mapper']
        tw_lookup.clearAnimated()
        tw_lookup.setAnimated()
        anim_list = []
        for n in sorted(value_dict.keys()):
            anim_list.append(nuke.AnimationKey(value_dict[n]/distance,n))
        anim = tw_lookup.animation(0)
        anim.addKey(anim_list)
        tw_lookup.setExpression('curve(x%1)+floor(x)')
