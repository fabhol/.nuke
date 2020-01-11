faberration = nuke.selectedNode()
with faberration:
    curve = nuke.toNode('TimeDissolve')['lut']
    samples = 100
    counter = 0
    previous_value = 0
    distance = 0
    dict = {}
    for n in xrange(0,samples):
        x = 1.0/(samples-1)*counter
        value = curve.getValueAt(x)
        if counter > 0:
            distance += abs(value-previous_value)
        dict[x] = distance
        previous_value = value
        counter += 1
    tw_lookup = nuke.toNode('TimeWarp')['lookup']
    tw_lookup.clearAnimated()
    tw_lookup.setAnimated()
    anim_list = []
    for n in dict.keys():
        anim_list.append(nuke.AnimationKey(dict[n]/distance, n))
    anim = tw_lookup.animation(0)
    anim.addKey(anim_list)
    tw_lookup.setExpression('curve(x%1)+floor(x)')
