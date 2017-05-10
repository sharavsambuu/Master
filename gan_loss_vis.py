import matplotlib.pyplot as plt
import numpy as np

# loss_file = open('loss.txt', 'r')
# loss_fix_file = open('loss-fix.txt', 'w+')
# loss_lines = loss_file.readlines()
# loss_fix_file.writelines(loss_lines[1::2])
# loss_file.close()
# loss_fix_file.close()
#
# raw_input()
log_folder = 'GAN/GAN_log/'

model_name = '2017-05-06_ImgCapFalse_word2vec_Vocab1000_Seq15_Batch128_EmbSize50_repeat_Noise50_PreInitNone_Dataset_all_flowers_WGAN'

data = np.genfromtxt(
	log_folder + model_name + "/loss.txt",
	delimiter=',',
	skip_header=1,
	skip_footer=0,
	names=['epoch', 'batch', 'g_loss', 'g_acc', 'd_loss_gen', 'd_acc_gen', 'd_loss_train', 'd_acc_train'])

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Accuracy - 15 seqLength - Two Flowers")
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Accuracy')

skip = 1
# ax1.plot(data['epoch'][::skip], data['d_acc_gen'][::skip], c='b', label='discriminator_fake_accuracy')
# ax1.plot(data['epoch'][::skip], data['d_acc_train'][::skip], c='g', label='discriminator_real_accuracy')
# ax1.plot(data['epoch'][::skip], data['g_acc'][::skip], c='r', label='generator_accuracy')

ax1.plot(data['epoch'][::skip], data['d_loss_gen'][::skip], c='b', label='discriminator_fake_accuracy')
ax1.plot(data['epoch'][::skip], data['d_loss_train'][::skip], c='g', label='discriminator_real_accuracy')
ax1.plot(data['epoch'][::skip], data['g_loss'][::skip], c='r', label='generator_accuracy')

leg = ax1.legend()

plt.show()
