r = (fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

    #define data
    data1 = [9, 4, 50, 20, 14, 3]
    labels1 = ['1', '1.5', '2', '2.5', '3', '3.5/4/4.5']
    colors = sns.color_palette('coolwarm')[0:5]

    ax1.pie(data1, labels = labels1, colors = colors, autopct='%.0f%%')
    ax1.set_title('Number of bathrooms Ventura', fontdict = {'fontsize' : 14})

    data2 = [9, 45, 40, 6]
    labels2 = [2, 3, 4, 5]

    ax2.pie(data2, labels = labels2, colors = colors, autopct='%.0f%%')
    ax2.set_title("Number of bedrooms Ventura", fontdict = {'fontsize' : 14})
    plt.tight_layout()
    sns.set(rc = {'figure.figsize':(10,6)}))
