FROM kotaimen/mapnik

RUN apt update \
    && apt install -y \
	rsync \
	sshpass

COPY ./ /home/mapnik/

WORKDIR /home/mapnik

#CMD ./render.sh
CMD bash
