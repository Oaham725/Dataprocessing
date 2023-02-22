dict = {1:'H',6:'C',7:'N',8:'O',16:'S'}


def traverse_datasets(hdf_file):
    import h5py
    import numpy as np
    np.set_printoptions(threshold=1e6)
    np.set_printoptions(suppress=True)

    def h5py_dataset_iterator(g, prefix=''):
        # key = "conformers"
        for key in g.keys():
            print(key)
            item = g[key]
            # print(item)
            path = '{}/{}'.format(prefix, key)
            # print(g[path])
            if isinstance(item, h5py.Dataset):  # test for dataset
                yield (path, item)
            elif isinstance(item, h5py.Group):  # test for group (go down)
                yield from h5py_dataset_iterator(item, path)

    with h5py.File(hdf_file, 'r') as f:
        for (path, dset) in h5py_dataset_iterator(f):
            if path[-2]=="n" and path[-1]=="s":
                # print(path[1:3])
                if path[1:4]=="dis":
                    txtname = str(path[1:10])
                    print(f[path])
                    path2 = path[0:10] + '/atomic_numbers'
                    A = np.array(f[path][:])
                    atomic_number = np.array(f[path2][:])
                    print(atom_num)
                    print(np.shape(A)[0])
                    for i in range(np.shape(A)[0]):
                        m = str(i)
                        newname = txtname + m + ".gjf"
                        # print(A[i:])
                        with open(newname, "w") as aha:
                            aha.write("%chk=" + txtname + m + ".chk\n")
                            aha.write("%nprocshared=30\n")
                            aha.write("%mem=60GB\n")
                            aha.write(
                                "#p B3LYP/6-311+G** int=fine opt freq=Raman nosymm\n")
                            aha.write(" \n")
                            aha.write(txtname + "\n")
                            aha.write("  \n")
                            aha.write("0 1\n")
                            for j in range(atom_num):
                                atom = dict[atomic_number[j]]
                                line = np.array(A[i][j])
                                # print("atom")
                                # print(line)
                                aha.write(atom + "   " + str(line[0] * 0.5291772086) + "   " + str(
                                    line[1] * 0.5291772086) + "   " + str(line[2] * 0.5291772086) + "\n")
                            aha.write("  \n")
                            aha.write("  \n")
                    # file_handle = open('%s.txt' % txtname, mode='w')
                    # file_handle.write(str(f[path2][:]))
                    # file_handle.write('\n')
                    # file_handle.write(str(len(f[path2][:])))
                    # file_handle.write('\n')
                    # file_handle.write(str(A))
                    # # file_handle.write(f[path].dtype)
                    # file_handle.write('\n')
                else:
                    print(path, dset)
                    # conf = f[path]
                    print(path)
                    txtname = str(path[1:8])
                    print(f[path])
                    path2 = path[0:8] + '/atomic_numbers'
                    atom_num = len(f[path2][:])
                    A = np.array(f[path][:])
                    atomic_number = np.array(f[path2][:])
                    print(atom_num)
                    print(np.shape(A)[0])
                    for i in range(np.shape(A)[0]):
                        m = str(i)
                        newname = txtname + m + ".gjf"
                        # print(A[i:])
                        with open(newname, "w") as aha:
                            aha.write("%chk=" + txtname + m + ".chk\n")
                            aha.write("%nprocshared=30\n")
                            aha.write("%mem=60GB\n")
                            aha.write(
                                "#p B3LYP/6-311+G** int=fine opt freq=Raman nosymm\n")
                            aha.write(" \n")
                            aha.write(txtname + "\n")
                            aha.write("  \n")
                            aha.write("0 1\n")
                            for j in range(atom_num):
                                atom = dict[atomic_number[j]]
                                line = np.array(A[i][j])
                                # print("atom")
                                # print(line)
                                aha.write(atom + "   " + str(line[0]*0.5291772086) +"   " + str(line[1]*0.5291772086) +"   " + str(line[2]*0.5291772086) + "\n")
                            aha.write("  \n")
                            aha.write("  \n")


                    # file_handle = open('%s.txt' % txtname, mode='w')
                    # file_handle.write(str(f[path2][:]))
                    # file_handle.write('\n')
                    # file_handle.write(str(len(f[path2][:])))
                    # file_handle.write('\n')
                    # file_handle.write(str(A))
                    # # file_handle.write(f[path].dtype)
                    # file_handle.write('\n')



    return None



# 传入路径即可
traverse_datasets('G:\\SPICE\\downloader\\SPICE.hdf5')